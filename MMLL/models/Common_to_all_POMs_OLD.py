# -*- coding: utf-8 -*-
'''
Collection of methods common to all POMs. To be inherited by the ML classes'''

__author__ = "Angel Navia-Vázquez"
__date__ = "Mar 2020"


#import requests
import json
import pickle
#import base64
import numpy as np
#import dill
from MMLL.Common_to_all_objects import Common_to_all_objects

class Common_to_all_POMs(Common_to_all_objects):
    """
    This class implements basic methods and protocols common to all POMs.
    To be inherited by the specific ML models. Not every method is used by every POM.
    """

    def __init__(self):
        """
        Create a :class:`Common_to_all_POMs` instance.

        Parameters
        ----------
        None

        """
        return

    def dill_it(self, x):
        return dill.dumps(x) 

    def undill_it(self, x):
        return dill.loads(x) 

    def sigm(self, x):
        """
        Computes the sigmoid function

        Parameters
        ----------
        x: float
            input value

        Returns
        -------
        sigm(x): float

        """
        return 1 / (1 + np.exp(-x))

    def cross_entropy(self, o, y, epsilon):
        """
        Computes the Cross-Entropy cost function

        Parameters
        ----------
        o: ndarray float
            estimated values

        y: ndarray float
            target values

        epsilon: float
            very small value to avoid numerical errors

        Returns
        -------
        cross_entropy: ndarray float

        """
        o = o * (1.0 - 2.0 * epsilon) + epsilon
        ce = - np.multiply(y.ravel(), np.log(o)) - np.multiply((1 - y.ravel()), np.log(1.0 - o))
        return ce

    def run_Master(self):
        """
        This is the Finite State Machine loop to be run at Masternode, it runs the following actions until the stop condition is met:
            - Process the received packets
            - Perform actions according to the state
            - Update the execution state

        Parameters
        ----------
            None
        """
        while self.FSMmaster.state != 'waiting_order':
            packet = None
            sender = None
            packet, sender = self.CheckNewPacket_master()
            #self.Update_State_Master()
            #self.ProcessReceivedPacket_Master(packet, sender)

    def serialize(self, x):
        """
        Serialize a given object.
        
        Parameters
        ----------
        x: arbitrary (typically a dictionary)
            Object to be serialized

        Returns
        -------
        Serialized object: string

        """
        return base64.b64encode(pickle.dumps(x)).decode('utf-8')

    def unserialize(self, x):
        """
        Unserialize a serialized object.
 
         Parameters
        ----------
        x: arbitrary (string)
            Object to be unserialized

        Returns
        -------
        Unserialized object: typically a dictionary
 
        """  
        return pickle.loads(base64.b64decode(x.encode()))


    def run_crypto(self):
        """
        This is the Finite State Machine loop to be run at Cryptonode, it runs the following actions until the stop condition is met:
            - Process the received packets
            - Perform actions according to the state
            - Update the execution state

        Parameters
        ----------
            None
        """

        self.display('Common Crypto is READY and waiting instructions.')
        self.terminate = False
        while not self.terminate:
            packet, sender = self.CheckNewPacket_crypto()

    def chekAllStates(self, condition):
        """
        Checks if all states are equal to the condition

         Parameters
        ----------
        condition: string (state name)
            State to be checked

        """
        try:
            all_active = True
            for waddr in self.workers_addresses:
                if self.state_dict[waddr] != condition:
                    all_active = False

            # Resetting states after checking
            if all_active:
                for waddr in self.workers_addresses:
                    self.state_dict[waddr] = ''
        except Exception as err:
            print('STOP AT chekAllStates CommontoallPOMS')
            import code
            code.interact(local=locals())


        return all_active


    def CheckNewPacket_master(self):
        """
        Checks if there is a new message in the Master queue. If so, process it. This operation is highly dependant on the communications library.

        Parameters
        ----------
            None
        """
        packet = None
        active_sender = None

        if self.comms.name == 'localflask':
            addresses2check = self.workers_addresses.copy()
            try:
                if self.cryptonode_address is not None:
                    addresses2check += [self.cryptonode_address]
            except:
                pass

            try:
                addresses2check = list(set( addresses2check + self.broadcast_addresses))
            except:
                print('STOP AT addresses2check' )
                import code
                code.interact(local=locals())

                pass

            #print("Listening: ", addresses2check)

            for sender in addresses2check:
                try:
                    packet = self.comms.receive(sender, timeout=0.01)
                    self.display(self.name + ' %s received %s from %s' % (self.master_address, packet['action'], sender))
                    active_sender = sender
                    self.ProcessReceivedPacket_Master(packet, sender)
                    self.Update_State_Master()
                    packet = None
                except Exception as err:
                    if 'Timeout when receiving' not in str(err):
                        if 'NewConnectionError' in str(err):
                            self.display('\n*************************** ERROR ***************************')
                            self.display('The Flask Server is not running!')
                            self.display("Execute 'python local_flask_server.py' in a separate console")
                            self.display('************************************************************')
                            exit()
                        else:
                            self.display('ERROR AT CheckNewPacket_master: %s' % str(err))
                            import code
                            code.interact(local=locals())

        if self.comms.name == 'pycloudmessenger':

            try:
                self.comms.pycloudmessenger_timeout_POMs456 > 0
            except:
                self.comms.pycloudmessenger_timeout_POMs456 = 0.1

            try:
                packet = self.comms.receive(self.comms.pycloudmessenger_timeout_POMs456)
                if packet is not None:
                    sender = self.receive_from[packet['sender']]
                    active_sender = sender
                    #self.display(self.name + ' %s received %s from %s' % (self.master_address, packet['action'], sender))
                    self.ProcessReceivedPacket_Master(packet, sender)
                    self.Update_State_Master()
                    packet = None
            except Exception as err:
                if 'Operation timeout reached' not in str(err):
                    if 'Operation timed out' not in str(err):
                        self.display('Unhandled ERROR AT CheckNewPacket_master: %s' % str(err))
                        import code
                        print('ERROR AT CheckNewPacket_master --------------')
                        import code
                        code.interact(local=locals())
                pass

        return packet, active_sender

    def CheckNewPacket_worker(self):
        """
        Checks if there is a new message in the Worker queue. If so, process it. This operation is highly dependant on the communications library.

        Parameters
        ----------
            None
        """
        packet = None
        sender = None

        if self.comms.name == 'localflask':
            try:
                # The worker can only know the address of the master
                #addresses2check = self.workers_addresses + [self.master_address]
                # Warning, roundrobin with the local flask is deactivated...

                addresses2check = []
                try:
                    addresses2check.append(self.cryptonode_address)
                except:
                    pass
                try:
                    addresses2check.append(self.master_address)
                except:
                    pass

                for sender in addresses2check:
                    try:
                        packet = self.comms.receive(sender, timeout=0.01)
                        self.display(self.name + ' %s received %s from %s' % (self.worker_address, packet['action'], sender))
                        #if str(self.worker_address) == '1':
                        #    print('STOP AT CheckNewPacket_worker_Common')
                        #    import code
                        #    code.interact(local=locals())
                        ## WARNING ProcessReceivedPacket_Worker is executed elsewhere
                        #self.ProcessReceivedPacket_Worker(packet, sender)
                    except Exception as err:
                        if 'Timeout when receiving' not in str(err):
                            if 'NewConnectionError' in str(err):
                                self.display('\n*************************** ERROR ***************************')
                                self.display('The Flask Server is not running!')
                                self.display("Execute 'python local_flask_server.py' in a separate console")
                                self.display('************************************************************')
                                exit()
                            else:
                                self.display('ERROR AT CheckNewPacket_worker: %s' % str(err))
                                #import code
                                #code.interact(local=locals())
            except Exception as err2:
                self.display('ERROR AT CheckNewPacket_worker: %s' % str(err2))
                import code
                code.interact(local=locals())

        if self.comms.name == 'pycloudmessenger':
            try:
                self.comms.pycloudmessenger_timeout_POMs456 > 0
            except:
                self.comms.pycloudmessenger_timeout_POMs456 = 0.1

            try:
                packet = self.comms.receive(self.comms.pycloudmessenger_timeout_POMs456)
                sender = packet['sender']
                self.display(self.name + ' %s received %s from %s through pycloudmessenger' % (self.worker_address, packet['action'], sender))
            except Exception as err:
                if 'Operation timeout reached' not in str(err):
                    if 'Operation timed out' not in str(err):
                        print('ERROR AT CheckNewPacket_worker')
                        self.display('Unhandled ERROR AT CheckNewPacket_worker: %s' % str(err))
                        import code
                        code.interact(local=locals())
                pass

        return packet, sender

    def CheckNewPacket_crypto(self):
        """
        Checks if there is a new message in the Crypto queue. If so, process it. This operation is highly dependant on the communications library.

        Parameters
        ----------
            None
        """
        packet = None
        sender = None

        if self.comms.name == 'localflask':
            try:
                addresses2check = [self.master_address]
                for sender in addresses2check:
                    try:
                        packet = self.comms.receive(sender, timeout=0.01)
                        self.display(self.name + ' %s received %s from %s' % (self.cryptonode_address, packet['action'], sender))
                        #if str(self.worker_address) == '1':
                        #    print('STOP AT CheckNewPacket_worker_Common')
                        #    import code
                        #    code.interact(local=locals())

                        self.ProcessReceivedPacket_Crypto(packet, sender)
                    except Exception as err:
                        if 'Timeout when receiving' not in str(err):
                            self.display('ERROR AT CheckNewPacket_crypto: %s' % str(err))
                            import code
                            code.interact(local=locals())
            except Exception as err2:
                self.display('ERROR AT CheckNewPacket_crypto: %s' % str(err2))
                import code
                code.interact(local=locals())

        if self.comms.name == 'pycloudmessenger':
            try:
                self.comms.pycloudmessenger_timeout_POMs456 > 0
            except:
                self.comms.pycloudmessenger_timeout_POMs456 = 0.1

            try:
                packet = self.comms.receive(self.comms.pycloudmessenger_timeout_POMs456)
                sender = packet['sender']
                self.display(self.name + ' %s received %s from %s through pycloudmessenger' % (self.cryptonode_address, packet['action'], sender))
                self.ProcessReceivedPacket_Crypto(packet, sender)

            except Exception as err:
                if 'Operation timeout reached' not in str(err):
                    if 'Operation timed out' not in str(err):
                        print('ERROR AT CheckNewPacket_crypto')
                        self.display('Unhandled ERROR AT CheckNewPacket_crypto: %s' % str(err))
                        import code
                        code.interact(local=locals())
                pass

        return packet, sender


    def crypto_mult_X(self, B):
        """
        Multiplies any matrix/vector encrypted with the previously stored at crypto X encr. This is only to be executed by some POM4 algorithms.

        Parameters
        ----------
        B: matrix, vector, or dictionary of matrix/vector of encrypted numbers
            matrix/vector to be multiplied by X

        Returns
        -------
        Multiplication result: matrix, vector, or dictionary of matrix/vector

        """
        try:
            # Checking if dictionary
            is_dictionary = type(B) is dict

            if not is_dictionary:

                # Checking size
                try:
                    scalar_value = False
                    M, N = B.shape
                except:  # scalar value
                    scalar_value = True


                # Blinding, keep Rbl_B for later deblinding...
                if not scalar_value:
                    # wT X
                    Rbl_B = np.random.normal(0, 2, (M, N))
                    try:
                        B_bl = B + Rbl_B
                    except:
                        print('ERROR AT crypto_mult_X: overflow???')
                        import code
                        code.interact(local=locals())                       
                        pass
                else:
                    # PENDING
                    print('ERROR AT crypto_mult_X: escalar value')
                    import code
                    code.interact(local=locals())

                B_bl_send = B_bl

            if is_dictionary:
                B_bl_dict = {}
                Rbl_B_dict = {}
                keys = list(B.keys())

                for key in keys:
                    B_ = B[key]
                    # Checking size
                    try:
                        scalar_value = False
                        M, N = B_.shape
                    except:  # scalar value
                        scalar_value = True

                    # Blinding, keep Rbl_B for later deblinding...
                    if not scalar_value:
                        Rbl_B = np.random.normal(0, 2, (M, N))
                        try: ### overflow for small key_size...                                        
                            B_bl = B_ + Rbl_B
                        except:
                            print('STOP AT common xxx, overflow???')
                            import code
                            code.interact(local=locals())
                            pass

                        '''
                            #aux = self.encrypter.encrypt(B_bl)
                            aux = self.decrypter.decrypt(B_bl)
                            print('Not overflow')
                        '''
                        B_bl_dict.update({key: B_bl})
                        Rbl_B_dict.update({key: Rbl_B})
                    else:
                        # PENDING
                        print('ERROR AT crypto_mult_X, dictionary: escalar value')
                        import code
                        code.interact(local=locals())
                B_bl_send = B_bl_dict


            self.FSMmaster.go_mult_XB(self, B_bl_send)
            self.run_Master()
            # returns self.XB_bl_encr_dict

            # deblinding results, data:
            # self.XB_bl_encr_dict  -> X * B , blinded
            # Rbl_B_dict --> blinding values for B
            # self.BX_dict --> blinding values for X
            # self.X_encr_dict --> encrypted values for X
            # B  --> encrypted values for B

            XB_encr_dict = {} # stores the multiplication without blinding

            for waddr in self.workers_addresses:
                if not is_dictionary: #check
                    X_encr = self.X_encr_dict[waddr]
                    MQ, NQ = Rbl_B.shape
                    B_encr = B
                    Rx = self.BX_dict[waddr]
                    Rb = Rbl_B
                    aux = self.XB_bl_encr_dict[waddr]
                    aux = aux - Rb * X_encr
                    aux = aux - B_encr * Rx 
                    aux = aux - Rb * Rx
                    XB_encr_dict.update({waddr: aux})

                if is_dictionary:  # the values in B change                  
                    X_encr = self.X_encr_dict[waddr]
                    B_encr = B[waddr]
                    Rx = self.BX_dict[waddr]
                    Rb = Rbl_B_dict[waddr]
                    aux = self.XB_bl_encr_dict[waddr]
                    aux = aux - X_encr * Rb
                    aux = aux - Rx * B_encr
                    aux = aux - Rx * Rb
                    XB_encr_dict.update({waddr: aux})
        except:
            print('ERROR AT crypto_mult_X: general')
            import code
            code.interact(local=locals())

        return XB_encr_dict

    def decrypt_model(self, model_encr):
        self.FSMmaster.go_decrypt_model(self, model_encr)
        self.run_Master()

        #self.model_decr_bl
        # deblinding

        #print('STOP AT deblinding')
        #import code
        #code.interact(local=locals())

        #print('COMMON decrypt_model')

        try:
            self.model_decr = {}
            for key in list(self.model_decr_bl.keys()):
                x_decr_bl = self.model_decr_bl[key]
                #print('COMMON decrypt_model BL:')
                #print(self.bl[key])
                #print(x_decr_bl)
                x = x_decr_bl - self.bl[key]
                #print(x)
                self.model_decr.update({key: x})
        except:
            print('ERROR AT COMMON decrypt_model')
            import code
            code.interact(local=locals())
            pass

        return self.model_decr



    # DELETE?????

    def crypto_mult(self, Aq_prodpk, Bq_prodpk):
        """
        Multiplies any matrix/vector A encrypted under prodpk with another B matrix also encrypted with prodpk. This is only to be executed by some POM4 algorithms.

        Parameters
        ----------
        Aq_prodpk: matrix, vector, or dictionary of matrix/vector of encrypted numbers
            matrix/vector to be multiplied by B

        Bq_prodpk: matrix, vector, or dictionary of matrix/vector of encrypted numbers
            matrix/vector to be multiplied by A

        Returns
        -------
        Multiplication result: matrix, vector, or dictionary of matrix/vector

        """

        # Result in:
        ABq_prodpk = None
        try:
            # Checking if dictionary
            is_Adictionary = type(Aq_prodpk) is dict
            is_Bdictionary = type(Bq_prodpk) is dict

            if not is_Adictionary:
                # Checking size
                try:
                    scalar_A = False
                    MA, NA = Aq_prodpk.shape
                except:  # scalar value
                    scalar_A = True

                # Blinding, keep Rbl_A for later deblinding...
                if scalar_A:
                    [Aq_prodpk_bl, Rbl_A] = self.cr.Blind_Trunc_BCP(Aq_prodpk, self.cr.ProdPK)
                else:
                    [Aq_prodpk_bl, Rbl_A] = self.cr.vBlind_Trunc_BCP(Aq_prodpk, self.cr.ProdPK)

                Aq_prodpk_bl_send = Aq_prodpk_bl

            if is_Adictionary:
                Aq_prodpk_bl_dict = {}
                Rbl_A_dict = {}
                keys = list(Aq_prodpk.keys())
                for key in keys:
                    Aq_prodpk_ = Aq_prodpk[key]
                    # Checking size
                    try:
                        scalar_A = False
                        M, N = Aq_prodpk_.shape
                    except:  # scalar value
                        scalar_A = True
                    # Blinding, keep Rbl_B for later deblinding...
                    if not scalar_A:
                        [Aq_prodpk_bl, Rbl_A] = self.cr.vBlind_Trunc_BCP(Aq_prodpk_, self.cr.ProdPK)
                        Aq_prodpk_bl_dict.update({key: Aq_prodpk_bl})
                        Rbl_A_dict.update({key: Rbl_A})
                    else:
                        # PENDING
                        print('ERROR AT crypto_mult, dictionary: escalar value')
                        import code
                        code.interact(local=locals())

                Aq_prodpk_bl_send = Aq_prodpk_bl_dict

            # B is another dictionary
            if is_Bdictionary:
                Bq_prodpk_bl_dict = {}
                Rbl_B_dict = {}
                keys = list(Bq_prodpk.keys())
                for key in keys:
                    Bq_prodpk_ = Bq_prodpk[key]
                    # Checking size
                    try:
                        scalar_B = False
                        M, N = Bq_prodpk_.shape
                    except:  # scalar value
                        scalar_B = True
                    # Blinding, keep Rbl_B for later deblinding...
                    if not scalar_B:
                        [Bq_prodpk_bl, Rbl_B] = self.cr.vBlind_Trunc_BCP(Bq_prodpk_, self.cr.ProdPK)
                        Bq_prodpk_bl_dict.update({key: Bq_prodpk_bl})
                        Rbl_B_dict.update({key: Rbl_B})
                    else:
                        # PENDING
                        print('ERROR AT crypto_mult, dictionary: escalar value')
                        import code
                        code.interact(local=locals())

                Bq_prodpk_bl_send = Bq_prodpk_bl_dict

            if not is_Bdictionary:

                # Checking size
                try:
                    scalar_B = False
                    MB, NB = Bq_prodpk.shape
                except:  # scalar value
                    scalar_B = True

                if scalar_B:
                    [Bq_prodpk_bl_send, Rbl_B] = self.cr.Blind_Trunc_BCP(Bq_prodpk, self.cr.ProdPK)
                else:
                    [Bq_prodpk_bl_send, Rbl_B] = self.cr.vBlind_Trunc_BCP(Bq_prodpk, self.cr.ProdPK)

        except:
            print('============ERROR at crypto_mult, part send ==========================')
            import code
            code.interact(local=locals())

        try:
            self.FSMmaster.go_mult_AB(self, Aq_prodpk_bl_send, Bq_prodpk_bl_send)
            self.run_Master()
            # returns self.ABq_prodpk_bl_dict
            # deblinding results
            # self.Bq_prodpk_dict
            # self.Rbl_X_dict
        except:
            print('============ERROR at crypto_mult go_mult_AB ==========================')
            import code
            code.interact(local=locals())

        try:

            if not is_Adictionary:
                ABq_prodpk_bl = self.ABq_prodpk_bl_dict

                if not scalar_A:
                    RA_bl = Rbl_A 

                if not is_Bdictionary:
                    if scalar_B and not scalar_A: # B is escalar, A is not, reshape B to A
                        BBq_prodpk = np.zeros((MA, NA), dtype=object)
                        BBq_prodpk[:, :] = Bq_prodpk
                        RB_bl = np.zeros((MA, NA), dtype=object)
                        RB_bl[:, :] = Rbl_B
                    if scalar_B and scalar_A:# A and B are both scalars
                        BBq_prodpk = Bq_prodpk
                        RB_bl = Rbl_B

                    if not scalar_B:  # B is another vector, check dimensions
                        if MA == MB:
                            BBq_prodpk = np.zeros((MA, NA), dtype=object)
                            BBq_prodpk[:, :] = Bq_prodpk
                            RB_bl = np.zeros((MA, NA), dtype=object)
                            RB_bl[:, :] = Rbl_B
                        else:
                            print('============ERROR at crypto_mult: different dimensions MB MA ======')
                            import code
                            code.interact(local=locals())
                try:
                    if scalar_A and scalar_B:
                        ABq_prodpk = self.cr.UnBlind_Product_Trunc_BCP(Aq_prodpk, BBq_prodpk, ABq_prodpk_bl, Rbl_A, RB_bl, self.cr.ProdPK)
                    else:
                        ABq_prodpk = self.cr.vUnBlind_Product_Trunc_BCP(Aq_prodpk, BBq_prodpk, ABq_prodpk_bl, Rbl_A, RB_bl, self.cr.ProdPK)   
                except:
                    print('============ERROR at crypto_mult unblind ==========================')
                    import code
                    code.interact(local=locals())

            if is_Adictionary:

                ABq_prodpk = {}
                for waddr in self.workers_addresses:
                    ABq_prodpk_bl = self.ABq_prodpk_bl_dict[waddr]
                    Aq_prodpk_ = Aq_prodpk[waddr]
                    MA, NA = Aq_prodpk_.shape
                    RA_bl = Rbl_A_dict[waddr]

                    if not is_Bdictionary:
                        try:  # Matrix
                            MB, NB = Bq_prodpk.shape
                        except:  # escalar
                            MB = None

                        if MB is None: # B is escalar
                            BBq_prodpk = np.zeros((MA, NA), dtype=object)
                            BBq_prodpk[:, :] = Bq_prodpk
                            RB_bl = np.zeros((MA, NA), dtype=object)
                            RB_bl[:, :] = Rbl_B

                    if is_Bdictionary:
                        BBq_prodpk = Bq_prodpk[waddr]
                        RB_bl = Rbl_B_dict[waddr]
                        try:  # Matrix
                            MB, NB = BBq_prodpk.shape
                        except:  # escalar
                            MB = None

                        if MB is None: # B is escalar
                            print('STOP AT crypto_mult: check this case')
                            import code
                            code.interact(local=locals())
                            BBq_prodpk = np.zeros((MA, NA), dtype=object)
                            BBq_prodpk[:, :] = Bq_prodpk
                            RB_bl = np.zeros((MA, NA), dtype=object)
                            RB_bl[:, :] = Rbl_B

                    ABq_prodpk_ = self.cr.vUnBlind_Product_Trunc_BCP(Aq_prodpk_, BBq_prodpk, ABq_prodpk_bl, RA_bl, RB_bl, self.cr.ProdPK)
                    ABq_prodpk.update({waddr: ABq_prodpk_})
        except:
            print('ERROR AT crypto_mult: after send')
            import code
            code.interact(local=locals())

        return ABq_prodpk

    def crypto_mult_XC(self, Cq_prodpk):
        """
        Multiplies any matrix/vector encrypted under prodpk with the previously stored X matrix also encrypted with prodpk. This is only to be executed by some POM4 algorithms.

        Parameters
        ----------
        Cq_prodpk: matrix, vector, or dictionary of matrix/vector of encrypted numbers
            matrix/vector to be multiplied by X

        Returns
        -------
        Multiplication result: matrix, vector, or dictionary of matrix/vector

        """

        try:
            NC = Cq_prodpk.shape[0]
            NI = Cq_prodpk.shape[1]
            # Blinding C
            Rbl_C_dict = {}
            Cq_prodpk_bl_dict = {}
            for kc in range(NC):
                c = Cq_prodpk[kc, :].reshape((1, NI))
                [Cq_prodpk_bl, Rbl_C] = self.cr.vBlind_Trunc_BCP(c, self.cr.ProdPK)
                Rbl_C_dict.update({kc: Rbl_C})
                Cq_prodpk_bl_dict.update({kc: Cq_prodpk_bl})
        except:
            print('ERROR AT crypto_mult_XC: part A')
            import code
            code.interact(local=locals())

        self.FSMmaster.go_mult_XC(self, Cq_prodpk_bl_dict)
        self.run_Master()
        #self.XCq_prodpk_bl_dict
        try:
            XCq_prodpk_dict = {}
            for kc in self.XCq_prodpk_bl_dict.keys():
                tmp_dict = {}
                for waddr in self.workers_addresses:
                    Xq_prodpk = self.Xq_prodpk_dict[waddr]
                    RX_bl = self.Rbl_X_dict[waddr]
                    MX, NX = Xq_prodpk.shape
                    CCq_prodpk = np.zeros((MX, NX), dtype=object)
                    CCq_prodpk[:, :] = self.Cq_prodpk[kc, :].reshape((1, self.NI))
                    RC_bl = np.zeros((MX, NX), dtype=object)
                    RC_bl[:, :] = Rbl_C_dict[kc]
                    XCq_prodpk_bl = self.XCq_prodpk_bl_dict[kc][waddr]
                    XCq_prodpk = self.cr.vUnBlind_Product_Trunc_BCP(Xq_prodpk, CCq_prodpk, XCq_prodpk_bl, RX_bl, RC_bl, self.cr.ProdPK)
                    # OK
                    # XCq = self.cr.vmasterDec_BCP(XCq_prodpk, self.cr.ProdPK)
                    # XC = self.cr.vQinv(XCq)
                    tmp_dict.update({waddr: XCq_prodpk})
                XCq_prodpk_dict.update({kc: tmp_dict})
        except:
            print('ERROR AT crypto_mult_XC: part B')
            import code
            code.interact(local=locals())
        return XCq_prodpk_dict

    def crypto_argmin_DXC(self, DXCq_prodpk):
        """
        Finds the minimum mosition of an encrypted vector uner prodpk. This is only to be executed by some POM4 algorithms.

        Parameters
        ----------
        DXCq_prodpk: vector to find the minimum position
            vector

        Returns
        -------
        Minimum position: integer

        """
        is_DXCq_prodpk_dictionary = type(DXCq_prodpk) is dict

        if is_DXCq_prodpk_dictionary:
            Rbl_DXC_dict = {}
            DXCq_prodpk_bl_dict = {}
            keys = list(DXCq_prodpk.keys())
            for key in keys:
                DXCq_prodpk_ = DXCq_prodpk[key]
                M, N = DXCq_prodpk_.shape

                # Rbl_A must be equal at every row
                [DXCq_prodpk_bl, Rbl_DXC] = self.cr.vBlind_Trunc_BCP(DXCq_prodpk_, self.cr.ProdPK, equal_row=True)
                Rbl_DXC_dict.update({key: Rbl_DXC})  # unused?
                DXCq_prodpk_bl_dict.update({key: DXCq_prodpk_bl})  # unsused?
                # CHECK DXCq = self.cr.vmasterDec_BCP(DXCq_prodpk_bl, self.cr.ProdPK)
                # CHECK self.cr.vQinv(DXCq)

        self.FSMmaster.go_argmin_DXC(self, DXCq_prodpk_bl_dict)
        self.run_Master()
        # self.argmin_dict
        return self.argmin_dict

    '''
    def crypto_compute_DXC(self):
        
        return
    '''