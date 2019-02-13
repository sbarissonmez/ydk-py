""" NHRP_MIB 

This MIB contains managed object definitions for the Next
Hop Resolution Procol, NHRP, as defined in RFC 2332 [17].

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class NHRPMIB(Entity):
    """
    
    
    .. attribute:: nhrpgeneralobjects
    
    	
    	**type**\:  :py:class:`NhrpGeneralObjects <ydk.models.cisco_ios_xe.NHRP_MIB.NHRPMIB.NhrpGeneralObjects>`
    
    	**config**\: False
    
    .. attribute:: nhrpcachetable
    
    	This table contains mappings between internetwork layer addresses and NBMA subnetwork layer addresses
    	**type**\:  :py:class:`NhrpCacheTable <ydk.models.cisco_ios_xe.NHRP_MIB.NHRPMIB.NhrpCacheTable>`
    
    	**config**\: False
    
    .. attribute:: nhrppurgereqtable
    
    	This table will track Purge Request Information
    	**type**\:  :py:class:`NhrpPurgeReqTable <ydk.models.cisco_ios_xe.NHRP_MIB.NHRPMIB.NhrpPurgeReqTable>`
    
    	**config**\: False
    
    .. attribute:: nhrpclienttable
    
    	Information about NHRP clients (NHCs) managed by this agent
    	**type**\:  :py:class:`NhrpClientTable <ydk.models.cisco_ios_xe.NHRP_MIB.NHRPMIB.NhrpClientTable>`
    
    	**config**\: False
    
    .. attribute:: nhrpclientregistrationtable
    
    	A table of Registration Request Information that needs to be maintained by the NHCs (clients)
    	**type**\:  :py:class:`NhrpClientRegistrationTable <ydk.models.cisco_ios_xe.NHRP_MIB.NHRPMIB.NhrpClientRegistrationTable>`
    
    	**config**\: False
    
    .. attribute:: nhrpclientnhstable
    
    	A table of NHSes that are available for use by this NHC (client). By default, the agent will add an entry to this table that corresponds to the client's default router
    	**type**\:  :py:class:`NhrpClientNhsTable <ydk.models.cisco_ios_xe.NHRP_MIB.NHRPMIB.NhrpClientNhsTable>`
    
    	**config**\: False
    
    .. attribute:: nhrpclientstattable
    
    	This table contains statistics collected by NHRP clients
    	**type**\:  :py:class:`NhrpClientStatTable <ydk.models.cisco_ios_xe.NHRP_MIB.NHRPMIB.NhrpClientStatTable>`
    
    	**config**\: False
    
    .. attribute:: nhrpservertable
    
    	This table contains information for a set of NHSes associated with this agent
    	**type**\:  :py:class:`NhrpServerTable <ydk.models.cisco_ios_xe.NHRP_MIB.NHRPMIB.NhrpServerTable>`
    
    	**config**\: False
    
    .. attribute:: nhrpservercachetable
    
    	This table extends the nhrpCacheTable for NHSes.  If the nhrpCacheTable has a row added due to an NHS or based on information regarding an NHS then a row is also added in this table.  The rows in this table will be created when rows in the nhrpCacheTable are created.  However, there may be rows created in the nhrpCacheTable which do not have corresponding rows in this table.  For example, if the nhrpCacheTable has a row added due to a Next Hop Client which is co\-resident on the same device as the NHS, a row will not be added to this table
    	**type**\:  :py:class:`NhrpServerCacheTable <ydk.models.cisco_ios_xe.NHRP_MIB.NHRPMIB.NhrpServerCacheTable>`
    
    	**config**\: False
    
    .. attribute:: nhrpservernhctable
    
    	A table of NHCs that are available for use by this NHS (Server)
    	**type**\:  :py:class:`NhrpServerNhcTable <ydk.models.cisco_ios_xe.NHRP_MIB.NHRPMIB.NhrpServerNhcTable>`
    
    	**config**\: False
    
    .. attribute:: nhrpserverstattable
    
    	Statistics collected by Next Hop Servers
    	**type**\:  :py:class:`NhrpServerStatTable <ydk.models.cisco_ios_xe.NHRP_MIB.NHRPMIB.NhrpServerStatTable>`
    
    	**config**\: False
    
    

    """

    _prefix = 'NHRP-MIB'
    _revision = '1999-08-26'

    def __init__(self):
        super(NHRPMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "NHRP-MIB"
        self.yang_parent_name = "NHRP-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("nhrpGeneralObjects", ("nhrpgeneralobjects", NHRPMIB.NhrpGeneralObjects)), ("nhrpCacheTable", ("nhrpcachetable", NHRPMIB.NhrpCacheTable)), ("nhrpPurgeReqTable", ("nhrppurgereqtable", NHRPMIB.NhrpPurgeReqTable)), ("nhrpClientTable", ("nhrpclienttable", NHRPMIB.NhrpClientTable)), ("nhrpClientRegistrationTable", ("nhrpclientregistrationtable", NHRPMIB.NhrpClientRegistrationTable)), ("nhrpClientNhsTable", ("nhrpclientnhstable", NHRPMIB.NhrpClientNhsTable)), ("nhrpClientStatTable", ("nhrpclientstattable", NHRPMIB.NhrpClientStatTable)), ("nhrpServerTable", ("nhrpservertable", NHRPMIB.NhrpServerTable)), ("nhrpServerCacheTable", ("nhrpservercachetable", NHRPMIB.NhrpServerCacheTable)), ("nhrpServerNhcTable", ("nhrpservernhctable", NHRPMIB.NhrpServerNhcTable)), ("nhrpServerStatTable", ("nhrpserverstattable", NHRPMIB.NhrpServerStatTable))])
        self._leafs = OrderedDict()

        self.nhrpgeneralobjects = NHRPMIB.NhrpGeneralObjects()
        self.nhrpgeneralobjects.parent = self
        self._children_name_map["nhrpgeneralobjects"] = "nhrpGeneralObjects"

        self.nhrpcachetable = NHRPMIB.NhrpCacheTable()
        self.nhrpcachetable.parent = self
        self._children_name_map["nhrpcachetable"] = "nhrpCacheTable"

        self.nhrppurgereqtable = NHRPMIB.NhrpPurgeReqTable()
        self.nhrppurgereqtable.parent = self
        self._children_name_map["nhrppurgereqtable"] = "nhrpPurgeReqTable"

        self.nhrpclienttable = NHRPMIB.NhrpClientTable()
        self.nhrpclienttable.parent = self
        self._children_name_map["nhrpclienttable"] = "nhrpClientTable"

        self.nhrpclientregistrationtable = NHRPMIB.NhrpClientRegistrationTable()
        self.nhrpclientregistrationtable.parent = self
        self._children_name_map["nhrpclientregistrationtable"] = "nhrpClientRegistrationTable"

        self.nhrpclientnhstable = NHRPMIB.NhrpClientNhsTable()
        self.nhrpclientnhstable.parent = self
        self._children_name_map["nhrpclientnhstable"] = "nhrpClientNhsTable"

        self.nhrpclientstattable = NHRPMIB.NhrpClientStatTable()
        self.nhrpclientstattable.parent = self
        self._children_name_map["nhrpclientstattable"] = "nhrpClientStatTable"

        self.nhrpservertable = NHRPMIB.NhrpServerTable()
        self.nhrpservertable.parent = self
        self._children_name_map["nhrpservertable"] = "nhrpServerTable"

        self.nhrpservercachetable = NHRPMIB.NhrpServerCacheTable()
        self.nhrpservercachetable.parent = self
        self._children_name_map["nhrpservercachetable"] = "nhrpServerCacheTable"

        self.nhrpservernhctable = NHRPMIB.NhrpServerNhcTable()
        self.nhrpservernhctable.parent = self
        self._children_name_map["nhrpservernhctable"] = "nhrpServerNhcTable"

        self.nhrpserverstattable = NHRPMIB.NhrpServerStatTable()
        self.nhrpserverstattable.parent = self
        self._children_name_map["nhrpserverstattable"] = "nhrpServerStatTable"
        self._segment_path = lambda: "NHRP-MIB:NHRP-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(NHRPMIB, [], name, value)


    class NhrpGeneralObjects(Entity):
        """
        
        
        .. attribute:: nhrpnextindex
        
        	This scalar is used for creating rows in the nhrpClientTable and the nhrpServerTable. The value of this variable is a currently unused value for nhrpClientIndex and nhrpServerIndex.     The value returned when reading this variable must be unique for the NHC's and NHS's indices associated with this row. Subsequent attempts to read this variable must return different values.  NOTE\:  this object exists in the General Group because it is to be used in establishing rows in the nhrpClientTable and the nhrpServerTable.  In other words, the value retrieved from this object could become the value of nhrpClientIndex and nhprServerIndex.  In the situation of an agent re\-initialization the value of this object must be saved in non\-volatile storage.  This variable will return the special value 0 if no new rows can be created
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        

        """

        _prefix = 'NHRP-MIB'
        _revision = '1999-08-26'

        def __init__(self):
            super(NHRPMIB.NhrpGeneralObjects, self).__init__()

            self.yang_name = "nhrpGeneralObjects"
            self.yang_parent_name = "NHRP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('nhrpnextindex', (YLeaf(YType.uint32, 'nhrpNextIndex'), ['int'])),
            ])
            self.nhrpnextindex = None
            self._segment_path = lambda: "nhrpGeneralObjects"
            self._absolute_path = lambda: "NHRP-MIB:NHRP-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(NHRPMIB.NhrpGeneralObjects, ['nhrpnextindex'], name, value)



    class NhrpCacheTable(Entity):
        """
        This table contains mappings between internetwork layer
        addresses and NBMA subnetwork layer addresses.
        
        .. attribute:: nhrpcacheentry
        
        	A cached mapping between an internetwork layer address and an NBMA address. Entries can be created by the network administrator using the nhrpCacheRowStatus column, or they may be added dynamically based on protocol operation (including NHRP, SCSP, and others, such as ATMARP).  When created based by NHRP protocol operations this entry is largely based on contents contained in the Client Information Entry (CIE).  Zero or more Client Information Entries (CIEs) may be included in the NHRP Packet. For a complete description of the CIE, refer to Section 5.2.0.1 of RFC 2332 [17]
        	**type**\: list of  		 :py:class:`NhrpCacheEntry <ydk.models.cisco_ios_xe.NHRP_MIB.NHRPMIB.NhrpCacheTable.NhrpCacheEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'NHRP-MIB'
        _revision = '1999-08-26'

        def __init__(self):
            super(NHRPMIB.NhrpCacheTable, self).__init__()

            self.yang_name = "nhrpCacheTable"
            self.yang_parent_name = "NHRP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("nhrpCacheEntry", ("nhrpcacheentry", NHRPMIB.NhrpCacheTable.NhrpCacheEntry))])
            self._leafs = OrderedDict()

            self.nhrpcacheentry = YList(self)
            self._segment_path = lambda: "nhrpCacheTable"
            self._absolute_path = lambda: "NHRP-MIB:NHRP-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(NHRPMIB.NhrpCacheTable, [], name, value)


        class NhrpCacheEntry(Entity):
            """
            A cached mapping between an internetwork layer address
            and an NBMA address. Entries can be created by the
            network administrator using the nhrpCacheRowStatus
            column, or they may be added dynamically based on
            protocol operation (including NHRP, SCSP, and others,
            such as ATMARP).
            
            When created based by NHRP protocol operations
            this entry is largely based on contents contained in
            the Client Information Entry (CIE).
            
            Zero or more Client Information Entries (CIEs) may be
            included in the NHRP Packet. For a complete description
            of the CIE, refer to Section 5.2.0.1 of
            RFC 2332 [17].
            
            .. attribute:: nhrpcacheinternetworkaddrtype  (key)
            
            	The internetwork layer address type of this Next Hop Resolution Cache entry. The value of this object indicates how to interpret the values of nhrpCacheInternetworkAddr and nhrpCacheNextHopInternetworkAddr
            	**type**\:  :py:class:`AddressFamilyNumbers <ydk.models.cisco_ios_xe.IANA_ADDRESS_FAMILY_NUMBERS_MIB.AddressFamilyNumbers>`
            
            	**config**\: False
            
            .. attribute:: nhrpcacheinternetworkaddr  (key)
            
            	The value of the internetwork address of the destination
            	**type**\: str
            
            	**length:** 0..64
            
            	**config**\: False
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            	**config**\: False
            
            .. attribute:: nhrpcacheindex  (key)
            
            	An identifier for this entry that has local significance within the scope of the General Group.  This identifier is used here to uniquely identify this row, and also used in the 'nhrpPurgeTable' for the value of the 'nhrpPurgeCacheIdentifier'
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpcacheprefixlength
            
            	The number of bits that define the internetwork layer prefix associated with the nhrpCacheInternetworkAddr
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: nhrpcachenexthopinternetworkaddr
            
            	The value of the internetwork address of the next hop
            	**type**\: str
            
            	**length:** 0..64
            
            	**config**\: False
            
            .. attribute:: nhrpcachenbmaaddrtype
            
            	The NBMA address type. The value of this object indicates how to interpret the values of nhrpCacheNbmaAddr and nhrpCacheNbmaSubaddr
            	**type**\:  :py:class:`AddressFamilyNumbers <ydk.models.cisco_ios_xe.IANA_ADDRESS_FAMILY_NUMBERS_MIB.AddressFamilyNumbers>`
            
            	**config**\: False
            
            .. attribute:: nhrpcachenbmaaddr
            
            	The value of the NBMA subnetwork address of the next hop
            	**type**\: str
            
            	**length:** 0..64
            
            	**config**\: False
            
            .. attribute:: nhrpcachenbmasubaddr
            
            	The value of the NBMA subaddress of the next hop. If there is no subaddress concept for the NBMA address family, this value will be a zero\-length OCTET STRING
            	**type**\: str
            
            	**length:** 0..64
            
            	**config**\: False
            
            .. attribute:: nhrpcachetype
            
            	An indication of how this cache entry was created. The values are\:  'other(1)'                   The entry was added by some                              other means.  'register(2)'                In a server, added based on a                              client registration.  'resolveAuthoritative(3)'    In a client, added based on                              receiving an Authoritative                              NHRP Resolution Reply.     'resolveNonauthoritative(4)' In a client, added based on                              receiving a Nonauthoritative                              NHRP Resolution Reply.  'transit(5)'                 In a transit server, added by                              examining a forwarded NHRP                              packet.  'administrativelyAdded(6)'   In a client or server,                              manually added by the                              administrator. The                              StorageType of this entry is                              reflected in                              'nhrpCacheStorageType'.  'atmarp(7)'                  The entry was added due to an                              ATMARP.  'scsp(8)'                    The entry was added due to                              SCSP.   When the entry is under creation using the nhrpCacheRowStatus column, the only value that can be specified by the administrator is 'administrativelyAdded'. Attempting to set any other value will cause an 'inconsistentValue' error.  The value cannot be modified once the entry is active
            	**type**\:  :py:class:`NhrpCacheType <ydk.models.cisco_ios_xe.NHRP_MIB.NHRPMIB.NhrpCacheTable.NhrpCacheEntry.NhrpCacheType>`
            
            	**config**\: False
            
            .. attribute:: nhrpcachestate
            
            	An indication of the state of this entry. The values are\:  'incomplete(1)' The client has sent a NHRP Resolution                 Request but has not yet received the                 NHRP Resolution Reply.   'ackReply(2)'   For a client or server, this is a                 cached valid mapping.  'nakReply(3)'   For a client or server, this is a                 cached NAK mapping
            	**type**\:  :py:class:`NhrpCacheState <ydk.models.cisco_ios_xe.NHRP_MIB.NHRPMIB.NhrpCacheTable.NhrpCacheEntry.NhrpCacheState>`
            
            	**config**\: False
            
            .. attribute:: nhrpcacheholdingtimevalid
            
            	True(1) is returned if the value of 'nhrpCacheType' is not 'administrativelyAdded'.  Since the value of 'nhrpCacheType' was not configured by a user, the value of 'nhrpCacheHoldingTime' is considered valid.  In other words, the value of 'nhrpCacheHoldingTime' represents the Holding Time for the cache Entry.  If 'nhrpCacheType has been configured by a user, (i.e. the value of 'nhrpCacheType' is 'administrativelyAdded') then false(2) will be returned. This indicates that the value of 'nhrpCacheHoldingTime' is undefined because this row could possibly be backed up in nonvolatile storage
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: nhrpcacheholdingtime
            
            	If the value of 'nhrpCacheHoldingTimeValid is true(1) then this object represents the number of seconds that the cache entry will remain in this table.  When this value reaches 0 (zero) the row should be deleted.  If the value of 'nhrpCacheHoldingTimeValid is false(2) then this object is undefined
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: nhrpcachenegotiatedmtu
            
            	The maximum transmission unit (MTU) that was negotiated or registered for this entity. In other words, this is the actual MTU being used
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: nhrpcachepreference
            
            	An object which reflects the Preference value of the Client Information Entry (CIE).  Zero or more Client Information Entries (CIEs) may be included in the NHRP Packet.  One of the fields in the CIE is the Preference.  For a complete description of the CIE, refer to Section 5.2.0.1 of  RFC 2332 [17]
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: nhrpcachestoragetype
            
            	This value only has meaning when the 'nhrpCacheType' has the value of 'administrativelyAdded'.  When the row is created due to being 'administrativelyAdded', this object reflects whether this row is kept in volatile storage and lost upon reboot or if this row is backed up by non\-volatile or permanent storage.  If the value of 'nhrpCacheType' has a value which is not 'administrativelyAdded, then the value of this object is 'other(1)'
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            	**config**\: False
            
            .. attribute:: nhrpcacherowstatus
            
            	An object that allows entries in this table to be created and deleted using the RowStatus convention
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            

            """

            _prefix = 'NHRP-MIB'
            _revision = '1999-08-26'

            def __init__(self):
                super(NHRPMIB.NhrpCacheTable.NhrpCacheEntry, self).__init__()

                self.yang_name = "nhrpCacheEntry"
                self.yang_parent_name = "nhrpCacheTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['nhrpcacheinternetworkaddrtype','nhrpcacheinternetworkaddr','ifindex','nhrpcacheindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('nhrpcacheinternetworkaddrtype', (YLeaf(YType.enumeration, 'nhrpCacheInternetworkAddrType'), [('ydk.models.cisco_ios_xe.IANA_ADDRESS_FAMILY_NUMBERS_MIB', 'AddressFamilyNumbers', '')])),
                    ('nhrpcacheinternetworkaddr', (YLeaf(YType.str, 'nhrpCacheInternetworkAddr'), ['str'])),
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('nhrpcacheindex', (YLeaf(YType.uint32, 'nhrpCacheIndex'), ['int'])),
                    ('nhrpcacheprefixlength', (YLeaf(YType.int32, 'nhrpCachePrefixLength'), ['int'])),
                    ('nhrpcachenexthopinternetworkaddr', (YLeaf(YType.str, 'nhrpCacheNextHopInternetworkAddr'), ['str'])),
                    ('nhrpcachenbmaaddrtype', (YLeaf(YType.enumeration, 'nhrpCacheNbmaAddrType'), [('ydk.models.cisco_ios_xe.IANA_ADDRESS_FAMILY_NUMBERS_MIB', 'AddressFamilyNumbers', '')])),
                    ('nhrpcachenbmaaddr', (YLeaf(YType.str, 'nhrpCacheNbmaAddr'), ['str'])),
                    ('nhrpcachenbmasubaddr', (YLeaf(YType.str, 'nhrpCacheNbmaSubaddr'), ['str'])),
                    ('nhrpcachetype', (YLeaf(YType.enumeration, 'nhrpCacheType'), [('ydk.models.cisco_ios_xe.NHRP_MIB', 'NHRPMIB', 'NhrpCacheTable.NhrpCacheEntry.NhrpCacheType')])),
                    ('nhrpcachestate', (YLeaf(YType.enumeration, 'nhrpCacheState'), [('ydk.models.cisco_ios_xe.NHRP_MIB', 'NHRPMIB', 'NhrpCacheTable.NhrpCacheEntry.NhrpCacheState')])),
                    ('nhrpcacheholdingtimevalid', (YLeaf(YType.boolean, 'nhrpCacheHoldingTimeValid'), ['bool'])),
                    ('nhrpcacheholdingtime', (YLeaf(YType.uint32, 'nhrpCacheHoldingTime'), ['int'])),
                    ('nhrpcachenegotiatedmtu', (YLeaf(YType.int32, 'nhrpCacheNegotiatedMtu'), ['int'])),
                    ('nhrpcachepreference', (YLeaf(YType.int32, 'nhrpCachePreference'), ['int'])),
                    ('nhrpcachestoragetype', (YLeaf(YType.enumeration, 'nhrpCacheStorageType'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'StorageType', '')])),
                    ('nhrpcacherowstatus', (YLeaf(YType.enumeration, 'nhrpCacheRowStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.nhrpcacheinternetworkaddrtype = None
                self.nhrpcacheinternetworkaddr = None
                self.ifindex = None
                self.nhrpcacheindex = None
                self.nhrpcacheprefixlength = None
                self.nhrpcachenexthopinternetworkaddr = None
                self.nhrpcachenbmaaddrtype = None
                self.nhrpcachenbmaaddr = None
                self.nhrpcachenbmasubaddr = None
                self.nhrpcachetype = None
                self.nhrpcachestate = None
                self.nhrpcacheholdingtimevalid = None
                self.nhrpcacheholdingtime = None
                self.nhrpcachenegotiatedmtu = None
                self.nhrpcachepreference = None
                self.nhrpcachestoragetype = None
                self.nhrpcacherowstatus = None
                self._segment_path = lambda: "nhrpCacheEntry" + "[nhrpCacheInternetworkAddrType='" + str(self.nhrpcacheinternetworkaddrtype) + "']" + "[nhrpCacheInternetworkAddr='" + str(self.nhrpcacheinternetworkaddr) + "']" + "[ifIndex='" + str(self.ifindex) + "']" + "[nhrpCacheIndex='" + str(self.nhrpcacheindex) + "']"
                self._absolute_path = lambda: "NHRP-MIB:NHRP-MIB/nhrpCacheTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(NHRPMIB.NhrpCacheTable.NhrpCacheEntry, ['nhrpcacheinternetworkaddrtype', 'nhrpcacheinternetworkaddr', 'ifindex', 'nhrpcacheindex', 'nhrpcacheprefixlength', 'nhrpcachenexthopinternetworkaddr', 'nhrpcachenbmaaddrtype', 'nhrpcachenbmaaddr', 'nhrpcachenbmasubaddr', 'nhrpcachetype', 'nhrpcachestate', 'nhrpcacheholdingtimevalid', 'nhrpcacheholdingtime', 'nhrpcachenegotiatedmtu', 'nhrpcachepreference', 'nhrpcachestoragetype', 'nhrpcacherowstatus'], name, value)

            class NhrpCacheState(Enum):
                """
                NhrpCacheState (Enum Class)

                An indication of the state of this entry. The values are\:

                'incomplete(1)' The client has sent a NHRP Resolution

                                Request but has not yet received the

                                NHRP Resolution Reply.

                'ackReply(2)'   For a client or server, this is a

                                cached valid mapping.

                'nakReply(3)'   For a client or server, this is a

                                cached NAK mapping.

                .. data:: incomplete = 1

                .. data:: ackReply = 2

                .. data:: nakReply = 3

                """

                incomplete = Enum.YLeaf(1, "incomplete")

                ackReply = Enum.YLeaf(2, "ackReply")

                nakReply = Enum.YLeaf(3, "nakReply")


            class NhrpCacheType(Enum):
                """
                NhrpCacheType (Enum Class)

                An indication of how this cache entry

                was created. The values are\:

                'other(1)'                   The entry was added by some

                                             other means.

                'register(2)'                In a server, added based on a

                                             client registration.

                'resolveAuthoritative(3)'    In a client, added based on

                                             receiving an Authoritative

                                             NHRP Resolution Reply.

                'resolveNonauthoritative(4)' In a client, added based on

                                             receiving a Nonauthoritative

                                             NHRP Resolution Reply.

                'transit(5)'                 In a transit server, added by

                                             examining a forwarded NHRP

                                             packet.

                'administrativelyAdded(6)'   In a client or server,

                                             manually added by the

                                             administrator. The

                                             StorageType of this entry is

                                             reflected in

                                             'nhrpCacheStorageType'.

                'atmarp(7)'                  The entry was added due to an

                                             ATMARP.

                'scsp(8)'                    The entry was added due to

                                             SCSP.

                When the entry is under creation using the

                nhrpCacheRowStatus column, the only value that can be

                specified by the administrator is 'administrativelyAdded'.

                Attempting to set any other value will cause an

                'inconsistentValue' error.

                The value cannot be modified once the entry is active.

                .. data:: other = 1

                .. data:: register = 2

                .. data:: resolveAuthoritative = 3

                .. data:: resoveNonauthoritative = 4

                .. data:: transit = 5

                .. data:: administrativelyAdded = 6

                .. data:: atmarp = 7

                .. data:: scsp = 8

                """

                other = Enum.YLeaf(1, "other")

                register = Enum.YLeaf(2, "register")

                resolveAuthoritative = Enum.YLeaf(3, "resolveAuthoritative")

                resoveNonauthoritative = Enum.YLeaf(4, "resoveNonauthoritative")

                transit = Enum.YLeaf(5, "transit")

                administrativelyAdded = Enum.YLeaf(6, "administrativelyAdded")

                atmarp = Enum.YLeaf(7, "atmarp")

                scsp = Enum.YLeaf(8, "scsp")





    class NhrpPurgeReqTable(Entity):
        """
        This table will track Purge Request Information.
        
        .. attribute:: nhrppurgereqentry
        
        	Information regarding a Purge Request
        	**type**\: list of  		 :py:class:`NhrpPurgeReqEntry <ydk.models.cisco_ios_xe.NHRP_MIB.NHRPMIB.NhrpPurgeReqTable.NhrpPurgeReqEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'NHRP-MIB'
        _revision = '1999-08-26'

        def __init__(self):
            super(NHRPMIB.NhrpPurgeReqTable, self).__init__()

            self.yang_name = "nhrpPurgeReqTable"
            self.yang_parent_name = "NHRP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("nhrpPurgeReqEntry", ("nhrppurgereqentry", NHRPMIB.NhrpPurgeReqTable.NhrpPurgeReqEntry))])
            self._leafs = OrderedDict()

            self.nhrppurgereqentry = YList(self)
            self._segment_path = lambda: "nhrpPurgeReqTable"
            self._absolute_path = lambda: "NHRP-MIB:NHRP-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(NHRPMIB.NhrpPurgeReqTable, [], name, value)


        class NhrpPurgeReqEntry(Entity):
            """
            Information regarding a Purge Request.
            
            .. attribute:: nhrppurgeindex  (key)
            
            	An index for this entry that has local significance within the scope of this table
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrppurgecacheidentifier
            
            	This object identifies which row in 'nhrpCacheTable' is being purged.  This object should have the same value as the 'nhrpCacheIndex' in the 'nhrpCacheTable'
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrppurgeprefixlength
            
            	In the case of NHRP Purge Requests, this specifies the equivalence class of addresses which match the first 'Prefix Length' bit positions of the Client Protocol Address specified in the Client Information Entry (CIE)
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: nhrppurgerequestid
            
            	The Request ID used in the purge request
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrppurgereplyexpected
            
            	An indication of whether this Purge Request has the 'N' Bit cleared (off)
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: nhrppurgerowstatus
            
            	An object that allows entries in this table to be created and deleted using the RowStatus convention
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            

            """

            _prefix = 'NHRP-MIB'
            _revision = '1999-08-26'

            def __init__(self):
                super(NHRPMIB.NhrpPurgeReqTable.NhrpPurgeReqEntry, self).__init__()

                self.yang_name = "nhrpPurgeReqEntry"
                self.yang_parent_name = "nhrpPurgeReqTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['nhrppurgeindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('nhrppurgeindex', (YLeaf(YType.uint32, 'nhrpPurgeIndex'), ['int'])),
                    ('nhrppurgecacheidentifier', (YLeaf(YType.uint32, 'nhrpPurgeCacheIdentifier'), ['int'])),
                    ('nhrppurgeprefixlength', (YLeaf(YType.int32, 'nhrpPurgePrefixLength'), ['int'])),
                    ('nhrppurgerequestid', (YLeaf(YType.uint32, 'nhrpPurgeRequestID'), ['int'])),
                    ('nhrppurgereplyexpected', (YLeaf(YType.boolean, 'nhrpPurgeReplyExpected'), ['bool'])),
                    ('nhrppurgerowstatus', (YLeaf(YType.enumeration, 'nhrpPurgeRowStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.nhrppurgeindex = None
                self.nhrppurgecacheidentifier = None
                self.nhrppurgeprefixlength = None
                self.nhrppurgerequestid = None
                self.nhrppurgereplyexpected = None
                self.nhrppurgerowstatus = None
                self._segment_path = lambda: "nhrpPurgeReqEntry" + "[nhrpPurgeIndex='" + str(self.nhrppurgeindex) + "']"
                self._absolute_path = lambda: "NHRP-MIB:NHRP-MIB/nhrpPurgeReqTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(NHRPMIB.NhrpPurgeReqTable.NhrpPurgeReqEntry, ['nhrppurgeindex', 'nhrppurgecacheidentifier', 'nhrppurgeprefixlength', 'nhrppurgerequestid', 'nhrppurgereplyexpected', 'nhrppurgerowstatus'], name, value)




    class NhrpClientTable(Entity):
        """
        Information about NHRP clients (NHCs) managed by this
        agent.
        
        .. attribute:: nhrpcliententry
        
        	Information about a single NHC
        	**type**\: list of  		 :py:class:`NhrpClientEntry <ydk.models.cisco_ios_xe.NHRP_MIB.NHRPMIB.NhrpClientTable.NhrpClientEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'NHRP-MIB'
        _revision = '1999-08-26'

        def __init__(self):
            super(NHRPMIB.NhrpClientTable, self).__init__()

            self.yang_name = "nhrpClientTable"
            self.yang_parent_name = "NHRP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("nhrpClientEntry", ("nhrpcliententry", NHRPMIB.NhrpClientTable.NhrpClientEntry))])
            self._leafs = OrderedDict()

            self.nhrpcliententry = YList(self)
            self._segment_path = lambda: "nhrpClientTable"
            self._absolute_path = lambda: "NHRP-MIB:NHRP-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(NHRPMIB.NhrpClientTable, [], name, value)


        class NhrpClientEntry(Entity):
            """
            Information about a single NHC.
            
            .. attribute:: nhrpclientindex  (key)
            
            	An identifier for the NHRP client that is unique within the scope of this agent.  The 'nhrpNextIndex' value should be consulted (read), prior to creating a row in this table, and the value returned from reading 'nhrpNextIndex' should be used as this object's value
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpclientinternetworkaddrtype
            
            	The type of the internetwork layer address of this client. This object indicates how the value of nhrpClientInternetworkAddr is to be interpreted
            	**type**\:  :py:class:`AddressFamilyNumbers <ydk.models.cisco_ios_xe.IANA_ADDRESS_FAMILY_NUMBERS_MIB.AddressFamilyNumbers>`
            
            	**config**\: False
            
            .. attribute:: nhrpclientinternetworkaddr
            
            	The value of the internetwork layer address of this client
            	**type**\: str
            
            	**length:** 0..64
            
            	**config**\: False
            
            .. attribute:: nhrpclientnbmaaddrtype
            
            	The type of the NBMA subnetwork address of this client. This object indicates how the values of nhrpClientNbmaAddr and nhrpClientNbmaSubaddr are to be interpreted
            	**type**\:  :py:class:`AddressFamilyNumbers <ydk.models.cisco_ios_xe.IANA_ADDRESS_FAMILY_NUMBERS_MIB.AddressFamilyNumbers>`
            
            	**config**\: False
            
            .. attribute:: nhrpclientnbmaaddr
            
            	The NBMA subnetwork address of this client
            	**type**\: str
            
            	**length:** 0..64
            
            	**config**\: False
            
            .. attribute:: nhrpclientnbmasubaddr
            
            	The NBMA subaddress of this client. For NBMA address families without a subaddress concept, this will be a zero\-length OCTET STRING
            	**type**\: str
            
            	**length:** 0..64
            
            	**config**\: False
            
            .. attribute:: nhrpclientinitialrequesttimeout
            
            	The number of seconds that the client will wait before timing out an NHRP initial request.  This object only has meaning for the initial timeout period
            	**type**\: int
            
            	**range:** 1..900
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: nhrpclientregistrationrequestretries
            
            	The number of times the client will retry the registration request before failure. A value of 0 means don't retry. A value of 65535 means retry forever
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: nhrpclientresolutionrequestretries
            
            	The number of times the client will retry the resolution request before failure. A value of 0 means don't retry. A value of 65535 means retry forever
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: nhrpclientpurgerequestretries
            
            	The number of times the client will retry a purge request before failure. A value of 0 means don't retry. A value of 65535 means retry forever
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: nhrpclientdefaultmtu
            
            	The default maximum transmission unit (MTU) of the LIS/LAG which this client should use. This object will be initialized by the agent to the default MTU of the LIS/LAG (which is 9180) unless a different MTU value is specified during creation of this Client
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: nhrpclientholdtime
            
            	The hold time the client will register
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: nhrpclientrequestid
            
            	The Request ID used to register this client with its server. According to Section 5.2.3 of the NHRP Specification, RFC 2332 [17], the Request ID must be kept in non\-volatile storage, so that if an NHC crashes and  re\-initializes, it will use a different  Request ID during the registration process when reregistering with the same NHS
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpclientstoragetype
            
            	This object defines whether this row is kept in volatile storage and lost upon a Client crash or reboot situation, or if this row is backed up by nonvolatile or permanent storage
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            	**config**\: False
            
            .. attribute:: nhrpclientrowstatus
            
            	An object that allows entries in this table to be created and deleted using the RowStatus convention
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            

            """

            _prefix = 'NHRP-MIB'
            _revision = '1999-08-26'

            def __init__(self):
                super(NHRPMIB.NhrpClientTable.NhrpClientEntry, self).__init__()

                self.yang_name = "nhrpClientEntry"
                self.yang_parent_name = "nhrpClientTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['nhrpclientindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('nhrpclientindex', (YLeaf(YType.uint32, 'nhrpClientIndex'), ['int'])),
                    ('nhrpclientinternetworkaddrtype', (YLeaf(YType.enumeration, 'nhrpClientInternetworkAddrType'), [('ydk.models.cisco_ios_xe.IANA_ADDRESS_FAMILY_NUMBERS_MIB', 'AddressFamilyNumbers', '')])),
                    ('nhrpclientinternetworkaddr', (YLeaf(YType.str, 'nhrpClientInternetworkAddr'), ['str'])),
                    ('nhrpclientnbmaaddrtype', (YLeaf(YType.enumeration, 'nhrpClientNbmaAddrType'), [('ydk.models.cisco_ios_xe.IANA_ADDRESS_FAMILY_NUMBERS_MIB', 'AddressFamilyNumbers', '')])),
                    ('nhrpclientnbmaaddr', (YLeaf(YType.str, 'nhrpClientNbmaAddr'), ['str'])),
                    ('nhrpclientnbmasubaddr', (YLeaf(YType.str, 'nhrpClientNbmaSubaddr'), ['str'])),
                    ('nhrpclientinitialrequesttimeout', (YLeaf(YType.int32, 'nhrpClientInitialRequestTimeout'), ['int'])),
                    ('nhrpclientregistrationrequestretries', (YLeaf(YType.int32, 'nhrpClientRegistrationRequestRetries'), ['int'])),
                    ('nhrpclientresolutionrequestretries', (YLeaf(YType.int32, 'nhrpClientResolutionRequestRetries'), ['int'])),
                    ('nhrpclientpurgerequestretries', (YLeaf(YType.int32, 'nhrpClientPurgeRequestRetries'), ['int'])),
                    ('nhrpclientdefaultmtu', (YLeaf(YType.uint32, 'nhrpClientDefaultMtu'), ['int'])),
                    ('nhrpclientholdtime', (YLeaf(YType.uint32, 'nhrpClientHoldTime'), ['int'])),
                    ('nhrpclientrequestid', (YLeaf(YType.uint32, 'nhrpClientRequestID'), ['int'])),
                    ('nhrpclientstoragetype', (YLeaf(YType.enumeration, 'nhrpClientStorageType'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'StorageType', '')])),
                    ('nhrpclientrowstatus', (YLeaf(YType.enumeration, 'nhrpClientRowStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.nhrpclientindex = None
                self.nhrpclientinternetworkaddrtype = None
                self.nhrpclientinternetworkaddr = None
                self.nhrpclientnbmaaddrtype = None
                self.nhrpclientnbmaaddr = None
                self.nhrpclientnbmasubaddr = None
                self.nhrpclientinitialrequesttimeout = None
                self.nhrpclientregistrationrequestretries = None
                self.nhrpclientresolutionrequestretries = None
                self.nhrpclientpurgerequestretries = None
                self.nhrpclientdefaultmtu = None
                self.nhrpclientholdtime = None
                self.nhrpclientrequestid = None
                self.nhrpclientstoragetype = None
                self.nhrpclientrowstatus = None
                self._segment_path = lambda: "nhrpClientEntry" + "[nhrpClientIndex='" + str(self.nhrpclientindex) + "']"
                self._absolute_path = lambda: "NHRP-MIB:NHRP-MIB/nhrpClientTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(NHRPMIB.NhrpClientTable.NhrpClientEntry, ['nhrpclientindex', 'nhrpclientinternetworkaddrtype', 'nhrpclientinternetworkaddr', 'nhrpclientnbmaaddrtype', 'nhrpclientnbmaaddr', 'nhrpclientnbmasubaddr', 'nhrpclientinitialrequesttimeout', 'nhrpclientregistrationrequestretries', 'nhrpclientresolutionrequestretries', 'nhrpclientpurgerequestretries', 'nhrpclientdefaultmtu', 'nhrpclientholdtime', 'nhrpclientrequestid', 'nhrpclientstoragetype', 'nhrpclientrowstatus'], name, value)




    class NhrpClientRegistrationTable(Entity):
        """
        A table of Registration Request Information that
        needs to be maintained by the NHCs (clients).
        
        .. attribute:: nhrpclientregistrationentry
        
        	An NHC needs to maintain registration request information between the NHC and the NHS.  An entry in this table represents information for a single registration request
        	**type**\: list of  		 :py:class:`NhrpClientRegistrationEntry <ydk.models.cisco_ios_xe.NHRP_MIB.NHRPMIB.NhrpClientRegistrationTable.NhrpClientRegistrationEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'NHRP-MIB'
        _revision = '1999-08-26'

        def __init__(self):
            super(NHRPMIB.NhrpClientRegistrationTable, self).__init__()

            self.yang_name = "nhrpClientRegistrationTable"
            self.yang_parent_name = "NHRP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("nhrpClientRegistrationEntry", ("nhrpclientregistrationentry", NHRPMIB.NhrpClientRegistrationTable.NhrpClientRegistrationEntry))])
            self._leafs = OrderedDict()

            self.nhrpclientregistrationentry = YList(self)
            self._segment_path = lambda: "nhrpClientRegistrationTable"
            self._absolute_path = lambda: "NHRP-MIB:NHRP-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(NHRPMIB.NhrpClientRegistrationTable, [], name, value)


        class NhrpClientRegistrationEntry(Entity):
            """
            An NHC needs to maintain registration request information
            between the NHC and the NHS.  An entry in this table
            represents information for a single registration request.
            
            .. attribute:: nhrpclientindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`nhrpclientindex <ydk.models.cisco_ios_xe.NHRP_MIB.NHRPMIB.NhrpClientTable.NhrpClientEntry>`
            
            	**config**\: False
            
            .. attribute:: nhrpclientregindex  (key)
            
            	An identifier for this entry such that it identifies a specific Registration Request from the NHC represented by the nhrpClientIndex
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpclientreguniqueness
            
            	The Uniqueness indicator for this Registration Request. If this object has the value of requestUnique(1), then the Uniqueness bit is set in the the NHRP Registration Request represented by this row.  The value cannot be changed once the row is created
            	**type**\:  :py:class:`NhrpClientRegUniqueness <ydk.models.cisco_ios_xe.NHRP_MIB.NHRPMIB.NhrpClientRegistrationTable.NhrpClientRegistrationEntry.NhrpClientRegUniqueness>`
            
            	**config**\: False
            
            .. attribute:: nhrpclientregstate
            
            	The registration state of this client. The values are\: 'other(1)'             The state of the registration                        request is not one of                        'registering',                        'ackRegisterReply' or                        'nakRegisterReply'.  'registering(2)'        A registration request has                         been issued and a registration                         reply is expected.  'ackRegisterReply(3)'   A positive registration reply                         has been received.  'nakRegisterReply(4)'   The client has received a                         negative registration                         reply (NAK)
            	**type**\:  :py:class:`NhrpClientRegState <ydk.models.cisco_ios_xe.NHRP_MIB.NHRPMIB.NhrpClientRegistrationTable.NhrpClientRegistrationEntry.NhrpClientRegState>`
            
            	**config**\: False
            
            .. attribute:: nhrpclientregrowstatus
            
            	An object that allows entries in this table to be created and deleted using the RowStatus convention
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            

            """

            _prefix = 'NHRP-MIB'
            _revision = '1999-08-26'

            def __init__(self):
                super(NHRPMIB.NhrpClientRegistrationTable.NhrpClientRegistrationEntry, self).__init__()

                self.yang_name = "nhrpClientRegistrationEntry"
                self.yang_parent_name = "nhrpClientRegistrationTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['nhrpclientindex','nhrpclientregindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('nhrpclientindex', (YLeaf(YType.str, 'nhrpClientIndex'), ['int'])),
                    ('nhrpclientregindex', (YLeaf(YType.uint32, 'nhrpClientRegIndex'), ['int'])),
                    ('nhrpclientreguniqueness', (YLeaf(YType.enumeration, 'nhrpClientRegUniqueness'), [('ydk.models.cisco_ios_xe.NHRP_MIB', 'NHRPMIB', 'NhrpClientRegistrationTable.NhrpClientRegistrationEntry.NhrpClientRegUniqueness')])),
                    ('nhrpclientregstate', (YLeaf(YType.enumeration, 'nhrpClientRegState'), [('ydk.models.cisco_ios_xe.NHRP_MIB', 'NHRPMIB', 'NhrpClientRegistrationTable.NhrpClientRegistrationEntry.NhrpClientRegState')])),
                    ('nhrpclientregrowstatus', (YLeaf(YType.enumeration, 'nhrpClientRegRowStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.nhrpclientindex = None
                self.nhrpclientregindex = None
                self.nhrpclientreguniqueness = None
                self.nhrpclientregstate = None
                self.nhrpclientregrowstatus = None
                self._segment_path = lambda: "nhrpClientRegistrationEntry" + "[nhrpClientIndex='" + str(self.nhrpclientindex) + "']" + "[nhrpClientRegIndex='" + str(self.nhrpclientregindex) + "']"
                self._absolute_path = lambda: "NHRP-MIB:NHRP-MIB/nhrpClientRegistrationTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(NHRPMIB.NhrpClientRegistrationTable.NhrpClientRegistrationEntry, ['nhrpclientindex', 'nhrpclientregindex', 'nhrpclientreguniqueness', 'nhrpclientregstate', 'nhrpclientregrowstatus'], name, value)

            class NhrpClientRegState(Enum):
                """
                NhrpClientRegState (Enum Class)

                The registration state of this client. The values are\:

                'other(1)'             The state of the registration

                                       request is not one of

                                       'registering',

                                       'ackRegisterReply' or

                                       'nakRegisterReply'.

                'registering(2)'        A registration request has

                                        been issued and a registration

                                        reply is expected.

                'ackRegisterReply(3)'   A positive registration reply

                                        has been received.

                'nakRegisterReply(4)'   The client has received a

                                        negative registration

                                        reply (NAK).

                .. data:: other = 1

                .. data:: registering = 2

                .. data:: ackRegisterReply = 3

                .. data:: nakRegisterReply = 4

                """

                other = Enum.YLeaf(1, "other")

                registering = Enum.YLeaf(2, "registering")

                ackRegisterReply = Enum.YLeaf(3, "ackRegisterReply")

                nakRegisterReply = Enum.YLeaf(4, "nakRegisterReply")


            class NhrpClientRegUniqueness(Enum):
                """
                NhrpClientRegUniqueness (Enum Class)

                The Uniqueness indicator for this Registration Request.

                If this object has the value of requestUnique(1), then

                the Uniqueness bit is set in the the NHRP Registration

                Request represented by this row.  The value cannot

                be changed once the row is created.

                .. data:: requestUnique = 1

                .. data:: requestNotUnique = 2

                """

                requestUnique = Enum.YLeaf(1, "requestUnique")

                requestNotUnique = Enum.YLeaf(2, "requestNotUnique")





    class NhrpClientNhsTable(Entity):
        """
        A table of NHSes that are available for use by this NHC
        (client). By default, the agent will add an entry to this
        table that corresponds to the client's default router.
        
        .. attribute:: nhrpclientnhsentry
        
        	An NHS that may be used by an NHC
        	**type**\: list of  		 :py:class:`NhrpClientNhsEntry <ydk.models.cisco_ios_xe.NHRP_MIB.NHRPMIB.NhrpClientNhsTable.NhrpClientNhsEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'NHRP-MIB'
        _revision = '1999-08-26'

        def __init__(self):
            super(NHRPMIB.NhrpClientNhsTable, self).__init__()

            self.yang_name = "nhrpClientNhsTable"
            self.yang_parent_name = "NHRP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("nhrpClientNhsEntry", ("nhrpclientnhsentry", NHRPMIB.NhrpClientNhsTable.NhrpClientNhsEntry))])
            self._leafs = OrderedDict()

            self.nhrpclientnhsentry = YList(self)
            self._segment_path = lambda: "nhrpClientNhsTable"
            self._absolute_path = lambda: "NHRP-MIB:NHRP-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(NHRPMIB.NhrpClientNhsTable, [], name, value)


        class NhrpClientNhsEntry(Entity):
            """
            An NHS that may be used by an NHC.
            
            .. attribute:: nhrpclientindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`nhrpclientindex <ydk.models.cisco_ios_xe.NHRP_MIB.NHRPMIB.NhrpClientTable.NhrpClientEntry>`
            
            	**config**\: False
            
            .. attribute:: nhrpclientnhsindex  (key)
            
            	An identifier for an NHS available to an NHC
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpclientnhsinternetworkaddrtype
            
            	The type of the internetwork layer address of the NHRP server represented in this entry. This object indicates how the value of nhrpClientNhsInternetworkAddr is to be interpreted
            	**type**\:  :py:class:`AddressFamilyNumbers <ydk.models.cisco_ios_xe.IANA_ADDRESS_FAMILY_NUMBERS_MIB.AddressFamilyNumbers>`
            
            	**config**\: False
            
            .. attribute:: nhrpclientnhsinternetworkaddr
            
            	The value of the destination internetwork layer address of the NHRP server represented by this    entry.  If this value is not known, this will be a zero\-length OCTET STRING
            	**type**\: str
            
            	**length:** 0..64
            
            	**config**\: False
            
            .. attribute:: nhrpclientnhsnbmaaddrtype
            
            	The type of the NBMA subnetwork address of the NHRP Server represented by this entry. This object indicates how the values of nhrpClientNhsNbmaAddr and nhrpClientNhsNbmaSubaddr are to be interpreted
            	**type**\:  :py:class:`AddressFamilyNumbers <ydk.models.cisco_ios_xe.IANA_ADDRESS_FAMILY_NUMBERS_MIB.AddressFamilyNumbers>`
            
            	**config**\: False
            
            .. attribute:: nhrpclientnhsnbmaaddr
            
            	The NBMA subnetwork address of the NHS. The type of the address is indicated by the corresponding value of nhrpClientNhsNbmaAddrType
            	**type**\: str
            
            	**length:** 0..64
            
            	**config**\: False
            
            .. attribute:: nhrpclientnhsnbmasubaddr
            
            	The NBMA subaddress of the NHS. For NMBA address families that do not have the concept of subaddress,      this will be a zero\-length OCTET STRING
            	**type**\: str
            
            	**length:** 0..64
            
            	**config**\: False
            
            .. attribute:: nhrpclientnhsinuse
            
            	An indication of whether this NHS is in use by the NHC
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: nhrpclientnhsrowstatus
            
            	An object that allows entries in this table to be created and deleted using the RowStatus convention
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            

            """

            _prefix = 'NHRP-MIB'
            _revision = '1999-08-26'

            def __init__(self):
                super(NHRPMIB.NhrpClientNhsTable.NhrpClientNhsEntry, self).__init__()

                self.yang_name = "nhrpClientNhsEntry"
                self.yang_parent_name = "nhrpClientNhsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['nhrpclientindex','nhrpclientnhsindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('nhrpclientindex', (YLeaf(YType.str, 'nhrpClientIndex'), ['int'])),
                    ('nhrpclientnhsindex', (YLeaf(YType.uint32, 'nhrpClientNhsIndex'), ['int'])),
                    ('nhrpclientnhsinternetworkaddrtype', (YLeaf(YType.enumeration, 'nhrpClientNhsInternetworkAddrType'), [('ydk.models.cisco_ios_xe.IANA_ADDRESS_FAMILY_NUMBERS_MIB', 'AddressFamilyNumbers', '')])),
                    ('nhrpclientnhsinternetworkaddr', (YLeaf(YType.str, 'nhrpClientNhsInternetworkAddr'), ['str'])),
                    ('nhrpclientnhsnbmaaddrtype', (YLeaf(YType.enumeration, 'nhrpClientNhsNbmaAddrType'), [('ydk.models.cisco_ios_xe.IANA_ADDRESS_FAMILY_NUMBERS_MIB', 'AddressFamilyNumbers', '')])),
                    ('nhrpclientnhsnbmaaddr', (YLeaf(YType.str, 'nhrpClientNhsNbmaAddr'), ['str'])),
                    ('nhrpclientnhsnbmasubaddr', (YLeaf(YType.str, 'nhrpClientNhsNbmaSubaddr'), ['str'])),
                    ('nhrpclientnhsinuse', (YLeaf(YType.boolean, 'nhrpClientNhsInUse'), ['bool'])),
                    ('nhrpclientnhsrowstatus', (YLeaf(YType.enumeration, 'nhrpClientNhsRowStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.nhrpclientindex = None
                self.nhrpclientnhsindex = None
                self.nhrpclientnhsinternetworkaddrtype = None
                self.nhrpclientnhsinternetworkaddr = None
                self.nhrpclientnhsnbmaaddrtype = None
                self.nhrpclientnhsnbmaaddr = None
                self.nhrpclientnhsnbmasubaddr = None
                self.nhrpclientnhsinuse = None
                self.nhrpclientnhsrowstatus = None
                self._segment_path = lambda: "nhrpClientNhsEntry" + "[nhrpClientIndex='" + str(self.nhrpclientindex) + "']" + "[nhrpClientNhsIndex='" + str(self.nhrpclientnhsindex) + "']"
                self._absolute_path = lambda: "NHRP-MIB:NHRP-MIB/nhrpClientNhsTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(NHRPMIB.NhrpClientNhsTable.NhrpClientNhsEntry, ['nhrpclientindex', 'nhrpclientnhsindex', 'nhrpclientnhsinternetworkaddrtype', 'nhrpclientnhsinternetworkaddr', 'nhrpclientnhsnbmaaddrtype', 'nhrpclientnhsnbmaaddr', 'nhrpclientnhsnbmasubaddr', 'nhrpclientnhsinuse', 'nhrpclientnhsrowstatus'], name, value)




    class NhrpClientStatTable(Entity):
        """
        This table contains statistics collected by NHRP
        clients.
        
        .. attribute:: nhrpclientstatentry
        
        	Statistics collected by a NHRP client
        	**type**\: list of  		 :py:class:`NhrpClientStatEntry <ydk.models.cisco_ios_xe.NHRP_MIB.NHRPMIB.NhrpClientStatTable.NhrpClientStatEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'NHRP-MIB'
        _revision = '1999-08-26'

        def __init__(self):
            super(NHRPMIB.NhrpClientStatTable, self).__init__()

            self.yang_name = "nhrpClientStatTable"
            self.yang_parent_name = "NHRP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("nhrpClientStatEntry", ("nhrpclientstatentry", NHRPMIB.NhrpClientStatTable.NhrpClientStatEntry))])
            self._leafs = OrderedDict()

            self.nhrpclientstatentry = YList(self)
            self._segment_path = lambda: "nhrpClientStatTable"
            self._absolute_path = lambda: "NHRP-MIB:NHRP-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(NHRPMIB.NhrpClientStatTable, [], name, value)


        class NhrpClientStatEntry(Entity):
            """
            Statistics collected by a NHRP client.
            
            .. attribute:: nhrpclientindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`nhrpclientindex <ydk.models.cisco_ios_xe.NHRP_MIB.NHRPMIB.NhrpClientTable.NhrpClientEntry>`
            
            	**config**\: False
            
            .. attribute:: nhrpclientstattxresolvereq
            
            	The number of NHRP Resolution Requests transmitted by this client.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpclientstatrxresolvereplyack
            
            	The number of positively acknowledged NHRP Resolution Replies received by this client.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpclientstatrxresolvereplynakprohibited
            
            	The number of NAKed NHRP Resolution Replies received by this client that contained the code indicating 'Administratively Prohibited'.   Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpclientstatrxresolvereplynakinsufresources
            
            	The number of NAKed NHRP Resolution Replies received by this client that contained the code indicating 'Insufficient Resources'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpclientstatrxresolvereplynaknobinding
            
            	The number of NAKed NHRP Resolution Replies received by this client that contained the code indicating 'No Internetworking Layer Address to NBMA Address Binding Exists'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpclientstatrxresolvereplynaknotunique
            
            	The number of NAKed NHRP Resolution Replies received by this client that contained the code indicating 'Binding Exists But Is Not Unique'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpclientstattxregisterreq
            
            	The number of NHRP Registration Requests transmitted by this client.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpclientstatrxregisterack
            
            	The number of positively acknowledged NHRP Registration Replies received by this client.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpclientstatrxregisternakprohibited
            
            	The number of NAKed NHRP Registration Replies received by this client that contained the code indicating 'Administratively Prohibited'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpclientstatrxregisternakinsufresources
            
            	The number of NAKed NHRP Registration Replies received by this client that contained the code indicating 'Insufficient Resources'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpclientstatrxregisternakalreadyreg
            
            	The number of NAKed NHRP Registration Replies received by this client that contained the code indicating 'Unique Internetworking Layer Address Already Registered'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpclientstatrxpurgereq
            
            	The number of NHRP Purge Requests received by this client.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpclientstattxpurgereq
            
            	The number of NHRP Purge Requests transmitted by this client.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpclientstatrxpurgereply
            
            	The number of NHRP Purge Replies received by this client.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpclientstattxpurgereply
            
            	The number of NHRP Purge Replies transmitted by this client.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpclientstattxerrorindication
            
            	The number of NHRP Error Indication packets transmitted by this client.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpclientstatrxerrunrecognizedextension
            
            	The number of NHRP Error Indication packets received by this client with the error code 'Unrecognized Extension'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpclientstatrxerrloopdetected
            
            	The number of NHRP Error Indication packets received by this client with the error code 'NHRP Loop Detected'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpclientstatrxerrprotoaddrunreachable
            
            	The number of NHRP Error Indication packets received by this client with the error code 'Protocol Address Unreachable'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpclientstatrxerrprotoerror
            
            	The number of NHRP Error Indication packets received by this client with the error code 'Protocol Error'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpclientstatrxerrsdusizeexceeded
            
            	The number of NHRP Error Indication packets received by this client with the error code 'NHRP SDU Size  Exceeded'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpclientstatrxerrinvalidextension
            
            	The number of NHRP Error Indication packets received by this client with the error code 'Invalid Extension'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpclientstatrxerrauthenticationfailure
            
            	The number of NHRP Error Indication packets received by this client with the error code 'Authentication Failure'.      Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpclientstatrxerrhopcountexceeded
            
            	The number of NHRP Error Indication packets received by this client with the error code 'Hop Count Exceeded'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpclientstatdiscontinuitytime
            
            	The value of sysUpTime on the most recent occasion at which any one or more of this Client's counters suffered a discontinuity.  If no such discontinuities have occurred since the last re\-initialization of the local management subsystem or the NHRP Client re\-initialization associated with this entry, then this object contains a zero value
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'NHRP-MIB'
            _revision = '1999-08-26'

            def __init__(self):
                super(NHRPMIB.NhrpClientStatTable.NhrpClientStatEntry, self).__init__()

                self.yang_name = "nhrpClientStatEntry"
                self.yang_parent_name = "nhrpClientStatTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['nhrpclientindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('nhrpclientindex', (YLeaf(YType.str, 'nhrpClientIndex'), ['int'])),
                    ('nhrpclientstattxresolvereq', (YLeaf(YType.uint32, 'nhrpClientStatTxResolveReq'), ['int'])),
                    ('nhrpclientstatrxresolvereplyack', (YLeaf(YType.uint32, 'nhrpClientStatRxResolveReplyAck'), ['int'])),
                    ('nhrpclientstatrxresolvereplynakprohibited', (YLeaf(YType.uint32, 'nhrpClientStatRxResolveReplyNakProhibited'), ['int'])),
                    ('nhrpclientstatrxresolvereplynakinsufresources', (YLeaf(YType.uint32, 'nhrpClientStatRxResolveReplyNakInsufResources'), ['int'])),
                    ('nhrpclientstatrxresolvereplynaknobinding', (YLeaf(YType.uint32, 'nhrpClientStatRxResolveReplyNakNoBinding'), ['int'])),
                    ('nhrpclientstatrxresolvereplynaknotunique', (YLeaf(YType.uint32, 'nhrpClientStatRxResolveReplyNakNotUnique'), ['int'])),
                    ('nhrpclientstattxregisterreq', (YLeaf(YType.uint32, 'nhrpClientStatTxRegisterReq'), ['int'])),
                    ('nhrpclientstatrxregisterack', (YLeaf(YType.uint32, 'nhrpClientStatRxRegisterAck'), ['int'])),
                    ('nhrpclientstatrxregisternakprohibited', (YLeaf(YType.uint32, 'nhrpClientStatRxRegisterNakProhibited'), ['int'])),
                    ('nhrpclientstatrxregisternakinsufresources', (YLeaf(YType.uint32, 'nhrpClientStatRxRegisterNakInsufResources'), ['int'])),
                    ('nhrpclientstatrxregisternakalreadyreg', (YLeaf(YType.uint32, 'nhrpClientStatRxRegisterNakAlreadyReg'), ['int'])),
                    ('nhrpclientstatrxpurgereq', (YLeaf(YType.uint32, 'nhrpClientStatRxPurgeReq'), ['int'])),
                    ('nhrpclientstattxpurgereq', (YLeaf(YType.uint32, 'nhrpClientStatTxPurgeReq'), ['int'])),
                    ('nhrpclientstatrxpurgereply', (YLeaf(YType.uint32, 'nhrpClientStatRxPurgeReply'), ['int'])),
                    ('nhrpclientstattxpurgereply', (YLeaf(YType.uint32, 'nhrpClientStatTxPurgeReply'), ['int'])),
                    ('nhrpclientstattxerrorindication', (YLeaf(YType.uint32, 'nhrpClientStatTxErrorIndication'), ['int'])),
                    ('nhrpclientstatrxerrunrecognizedextension', (YLeaf(YType.uint32, 'nhrpClientStatRxErrUnrecognizedExtension'), ['int'])),
                    ('nhrpclientstatrxerrloopdetected', (YLeaf(YType.uint32, 'nhrpClientStatRxErrLoopDetected'), ['int'])),
                    ('nhrpclientstatrxerrprotoaddrunreachable', (YLeaf(YType.uint32, 'nhrpClientStatRxErrProtoAddrUnreachable'), ['int'])),
                    ('nhrpclientstatrxerrprotoerror', (YLeaf(YType.uint32, 'nhrpClientStatRxErrProtoError'), ['int'])),
                    ('nhrpclientstatrxerrsdusizeexceeded', (YLeaf(YType.uint32, 'nhrpClientStatRxErrSduSizeExceeded'), ['int'])),
                    ('nhrpclientstatrxerrinvalidextension', (YLeaf(YType.uint32, 'nhrpClientStatRxErrInvalidExtension'), ['int'])),
                    ('nhrpclientstatrxerrauthenticationfailure', (YLeaf(YType.uint32, 'nhrpClientStatRxErrAuthenticationFailure'), ['int'])),
                    ('nhrpclientstatrxerrhopcountexceeded', (YLeaf(YType.uint32, 'nhrpClientStatRxErrHopCountExceeded'), ['int'])),
                    ('nhrpclientstatdiscontinuitytime', (YLeaf(YType.uint32, 'nhrpClientStatDiscontinuityTime'), ['int'])),
                ])
                self.nhrpclientindex = None
                self.nhrpclientstattxresolvereq = None
                self.nhrpclientstatrxresolvereplyack = None
                self.nhrpclientstatrxresolvereplynakprohibited = None
                self.nhrpclientstatrxresolvereplynakinsufresources = None
                self.nhrpclientstatrxresolvereplynaknobinding = None
                self.nhrpclientstatrxresolvereplynaknotunique = None
                self.nhrpclientstattxregisterreq = None
                self.nhrpclientstatrxregisterack = None
                self.nhrpclientstatrxregisternakprohibited = None
                self.nhrpclientstatrxregisternakinsufresources = None
                self.nhrpclientstatrxregisternakalreadyreg = None
                self.nhrpclientstatrxpurgereq = None
                self.nhrpclientstattxpurgereq = None
                self.nhrpclientstatrxpurgereply = None
                self.nhrpclientstattxpurgereply = None
                self.nhrpclientstattxerrorindication = None
                self.nhrpclientstatrxerrunrecognizedextension = None
                self.nhrpclientstatrxerrloopdetected = None
                self.nhrpclientstatrxerrprotoaddrunreachable = None
                self.nhrpclientstatrxerrprotoerror = None
                self.nhrpclientstatrxerrsdusizeexceeded = None
                self.nhrpclientstatrxerrinvalidextension = None
                self.nhrpclientstatrxerrauthenticationfailure = None
                self.nhrpclientstatrxerrhopcountexceeded = None
                self.nhrpclientstatdiscontinuitytime = None
                self._segment_path = lambda: "nhrpClientStatEntry" + "[nhrpClientIndex='" + str(self.nhrpclientindex) + "']"
                self._absolute_path = lambda: "NHRP-MIB:NHRP-MIB/nhrpClientStatTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(NHRPMIB.NhrpClientStatTable.NhrpClientStatEntry, ['nhrpclientindex', 'nhrpclientstattxresolvereq', 'nhrpclientstatrxresolvereplyack', 'nhrpclientstatrxresolvereplynakprohibited', 'nhrpclientstatrxresolvereplynakinsufresources', 'nhrpclientstatrxresolvereplynaknobinding', 'nhrpclientstatrxresolvereplynaknotunique', 'nhrpclientstattxregisterreq', 'nhrpclientstatrxregisterack', 'nhrpclientstatrxregisternakprohibited', 'nhrpclientstatrxregisternakinsufresources', 'nhrpclientstatrxregisternakalreadyreg', 'nhrpclientstatrxpurgereq', 'nhrpclientstattxpurgereq', 'nhrpclientstatrxpurgereply', 'nhrpclientstattxpurgereply', 'nhrpclientstattxerrorindication', 'nhrpclientstatrxerrunrecognizedextension', 'nhrpclientstatrxerrloopdetected', 'nhrpclientstatrxerrprotoaddrunreachable', 'nhrpclientstatrxerrprotoerror', 'nhrpclientstatrxerrsdusizeexceeded', 'nhrpclientstatrxerrinvalidextension', 'nhrpclientstatrxerrauthenticationfailure', 'nhrpclientstatrxerrhopcountexceeded', 'nhrpclientstatdiscontinuitytime'], name, value)




    class NhrpServerTable(Entity):
        """
        This table contains information for a set of NHSes
        associated with this agent.
        
        .. attribute:: nhrpserverentry
        
        	Information about a single NHS
        	**type**\: list of  		 :py:class:`NhrpServerEntry <ydk.models.cisco_ios_xe.NHRP_MIB.NHRPMIB.NhrpServerTable.NhrpServerEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'NHRP-MIB'
        _revision = '1999-08-26'

        def __init__(self):
            super(NHRPMIB.NhrpServerTable, self).__init__()

            self.yang_name = "nhrpServerTable"
            self.yang_parent_name = "NHRP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("nhrpServerEntry", ("nhrpserverentry", NHRPMIB.NhrpServerTable.NhrpServerEntry))])
            self._leafs = OrderedDict()

            self.nhrpserverentry = YList(self)
            self._segment_path = lambda: "nhrpServerTable"
            self._absolute_path = lambda: "NHRP-MIB:NHRP-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(NHRPMIB.NhrpServerTable, [], name, value)


        class NhrpServerEntry(Entity):
            """
            Information about a single NHS.
            
            .. attribute:: nhrpserverindex  (key)
            
            	An identifier for the server that is unique within the scope of this agent
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpserverinternetworkaddrtype
            
            	The type of the internetwork layer address of this server. This object is used to interpret the value of nhrpServerInternetworkAddr
            	**type**\:  :py:class:`AddressFamilyNumbers <ydk.models.cisco_ios_xe.IANA_ADDRESS_FAMILY_NUMBERS_MIB.AddressFamilyNumbers>`
            
            	**config**\: False
            
            .. attribute:: nhrpserverinternetworkaddr
            
            	The value of the internetwork layer address of this server
            	**type**\: str
            
            	**length:** 0..64
            
            	**config**\: False
            
            .. attribute:: nhrpservernbmaaddrtype
            
            	The type of the NBMA subnetwork address of this server. This object is used to interpret the value of nhrpServerNbmaAddr
            	**type**\:  :py:class:`AddressFamilyNumbers <ydk.models.cisco_ios_xe.IANA_ADDRESS_FAMILY_NUMBERS_MIB.AddressFamilyNumbers>`
            
            	**config**\: False
            
            .. attribute:: nhrpservernbmaaddr
            
            	The value of the NBMA subnetwork address of this server
            	**type**\: str
            
            	**length:** 0..64
            
            	**config**\: False
            
            .. attribute:: nhrpservernbmasubaddr
            
            	The value of the NBMA subaddress of this server. For NBMA address families without a subaddress concept, this will be a zero\-length OCTET STRING
            	**type**\: str
            
            	**length:** 0..64
            
            	**config**\: False
            
            .. attribute:: nhrpserverstoragetype
            
            	This object defines whether this row is kept in volatile storage and lost upon a Server crash or reboot situation, or if this row is backed up by nonvolatile or permanent storage
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            	**config**\: False
            
            .. attribute:: nhrpserverrowstatus
            
            	An object that allows entries in this table to be created and deleted using the RowStatus convention
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            

            """

            _prefix = 'NHRP-MIB'
            _revision = '1999-08-26'

            def __init__(self):
                super(NHRPMIB.NhrpServerTable.NhrpServerEntry, self).__init__()

                self.yang_name = "nhrpServerEntry"
                self.yang_parent_name = "nhrpServerTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['nhrpserverindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('nhrpserverindex', (YLeaf(YType.uint32, 'nhrpServerIndex'), ['int'])),
                    ('nhrpserverinternetworkaddrtype', (YLeaf(YType.enumeration, 'nhrpServerInternetworkAddrType'), [('ydk.models.cisco_ios_xe.IANA_ADDRESS_FAMILY_NUMBERS_MIB', 'AddressFamilyNumbers', '')])),
                    ('nhrpserverinternetworkaddr', (YLeaf(YType.str, 'nhrpServerInternetworkAddr'), ['str'])),
                    ('nhrpservernbmaaddrtype', (YLeaf(YType.enumeration, 'nhrpServerNbmaAddrType'), [('ydk.models.cisco_ios_xe.IANA_ADDRESS_FAMILY_NUMBERS_MIB', 'AddressFamilyNumbers', '')])),
                    ('nhrpservernbmaaddr', (YLeaf(YType.str, 'nhrpServerNbmaAddr'), ['str'])),
                    ('nhrpservernbmasubaddr', (YLeaf(YType.str, 'nhrpServerNbmaSubaddr'), ['str'])),
                    ('nhrpserverstoragetype', (YLeaf(YType.enumeration, 'nhrpServerStorageType'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'StorageType', '')])),
                    ('nhrpserverrowstatus', (YLeaf(YType.enumeration, 'nhrpServerRowStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.nhrpserverindex = None
                self.nhrpserverinternetworkaddrtype = None
                self.nhrpserverinternetworkaddr = None
                self.nhrpservernbmaaddrtype = None
                self.nhrpservernbmaaddr = None
                self.nhrpservernbmasubaddr = None
                self.nhrpserverstoragetype = None
                self.nhrpserverrowstatus = None
                self._segment_path = lambda: "nhrpServerEntry" + "[nhrpServerIndex='" + str(self.nhrpserverindex) + "']"
                self._absolute_path = lambda: "NHRP-MIB:NHRP-MIB/nhrpServerTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(NHRPMIB.NhrpServerTable.NhrpServerEntry, ['nhrpserverindex', 'nhrpserverinternetworkaddrtype', 'nhrpserverinternetworkaddr', 'nhrpservernbmaaddrtype', 'nhrpservernbmaaddr', 'nhrpservernbmasubaddr', 'nhrpserverstoragetype', 'nhrpserverrowstatus'], name, value)




    class NhrpServerCacheTable(Entity):
        """
        This table extends the nhrpCacheTable for
        NHSes.  If the nhrpCacheTable has a row added due to
        an NHS or based on information regarding an NHS then
        a row is also added in this table.
        
        The rows in this table will be created when rows in
        the nhrpCacheTable are created.  However, there may
        be rows created in the nhrpCacheTable which do not
        have corresponding rows in this table.  For example,
        if the nhrpCacheTable has a row added due to a Next
        Hop Client which is co\-resident on the same device
        as the NHS, a row will not be added to this table.
        
        .. attribute:: nhrpservercacheentry
        
        	Additional information kept by a NHS for a relevant Next Hop Resolution Cache entry
        	**type**\: list of  		 :py:class:`NhrpServerCacheEntry <ydk.models.cisco_ios_xe.NHRP_MIB.NHRPMIB.NhrpServerCacheTable.NhrpServerCacheEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'NHRP-MIB'
        _revision = '1999-08-26'

        def __init__(self):
            super(NHRPMIB.NhrpServerCacheTable, self).__init__()

            self.yang_name = "nhrpServerCacheTable"
            self.yang_parent_name = "NHRP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("nhrpServerCacheEntry", ("nhrpservercacheentry", NHRPMIB.NhrpServerCacheTable.NhrpServerCacheEntry))])
            self._leafs = OrderedDict()

            self.nhrpservercacheentry = YList(self)
            self._segment_path = lambda: "nhrpServerCacheTable"
            self._absolute_path = lambda: "NHRP-MIB:NHRP-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(NHRPMIB.NhrpServerCacheTable, [], name, value)


        class NhrpServerCacheEntry(Entity):
            """
            Additional information kept by a NHS for a relevant
            Next Hop Resolution Cache entry.
            
            .. attribute:: nhrpcacheinternetworkaddrtype  (key)
            
            	
            	**type**\:  :py:class:`AddressFamilyNumbers <ydk.models.cisco_ios_xe.IANA_ADDRESS_FAMILY_NUMBERS_MIB.AddressFamilyNumbers>`
            
            	**config**\: False
            
            .. attribute:: nhrpcacheinternetworkaddr  (key)
            
            	
            	**type**\: str
            
            	**length:** 0..64
            
            	**refers to**\:  :py:class:`nhrpcacheinternetworkaddr <ydk.models.cisco_ios_xe.NHRP_MIB.NHRPMIB.NhrpCacheTable.NhrpCacheEntry>`
            
            	**config**\: False
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            	**config**\: False
            
            .. attribute:: nhrpcacheindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`nhrpcacheindex <ydk.models.cisco_ios_xe.NHRP_MIB.NHRPMIB.NhrpCacheTable.NhrpCacheEntry>`
            
            	**config**\: False
            
            .. attribute:: nhrpservercacheauthoritative
            
            	An indication of whether this cache entry is authoritative, which means the entry was added because of a direct registration request with this server or by Server Cache Synchronization Protocol (SCSP) from an authoritative source
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: nhrpservercacheuniqueness
            
            	The Uniqueness indicator for this cache entry used in duplicate address detection. This value cannot be changed after the entry is active
            	**type**\: bool
            
            	**config**\: False
            
            

            """

            _prefix = 'NHRP-MIB'
            _revision = '1999-08-26'

            def __init__(self):
                super(NHRPMIB.NhrpServerCacheTable.NhrpServerCacheEntry, self).__init__()

                self.yang_name = "nhrpServerCacheEntry"
                self.yang_parent_name = "nhrpServerCacheTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['nhrpcacheinternetworkaddrtype','nhrpcacheinternetworkaddr','ifindex','nhrpcacheindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('nhrpcacheinternetworkaddrtype', (YLeaf(YType.enumeration, 'nhrpCacheInternetworkAddrType'), [('ydk.models.cisco_ios_xe.IANA_ADDRESS_FAMILY_NUMBERS_MIB', 'AddressFamilyNumbers', '')])),
                    ('nhrpcacheinternetworkaddr', (YLeaf(YType.str, 'nhrpCacheInternetworkAddr'), ['str'])),
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('nhrpcacheindex', (YLeaf(YType.str, 'nhrpCacheIndex'), ['int'])),
                    ('nhrpservercacheauthoritative', (YLeaf(YType.boolean, 'nhrpServerCacheAuthoritative'), ['bool'])),
                    ('nhrpservercacheuniqueness', (YLeaf(YType.boolean, 'nhrpServerCacheUniqueness'), ['bool'])),
                ])
                self.nhrpcacheinternetworkaddrtype = None
                self.nhrpcacheinternetworkaddr = None
                self.ifindex = None
                self.nhrpcacheindex = None
                self.nhrpservercacheauthoritative = None
                self.nhrpservercacheuniqueness = None
                self._segment_path = lambda: "nhrpServerCacheEntry" + "[nhrpCacheInternetworkAddrType='" + str(self.nhrpcacheinternetworkaddrtype) + "']" + "[nhrpCacheInternetworkAddr='" + str(self.nhrpcacheinternetworkaddr) + "']" + "[ifIndex='" + str(self.ifindex) + "']" + "[nhrpCacheIndex='" + str(self.nhrpcacheindex) + "']"
                self._absolute_path = lambda: "NHRP-MIB:NHRP-MIB/nhrpServerCacheTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(NHRPMIB.NhrpServerCacheTable.NhrpServerCacheEntry, ['nhrpcacheinternetworkaddrtype', 'nhrpcacheinternetworkaddr', 'ifindex', 'nhrpcacheindex', 'nhrpservercacheauthoritative', 'nhrpservercacheuniqueness'], name, value)




    class NhrpServerNhcTable(Entity):
        """
        A table of NHCs that are available for use by this NHS
        (Server).
        
        .. attribute:: nhrpservernhcentry
        
        	An NHC that may be used by an NHS
        	**type**\: list of  		 :py:class:`NhrpServerNhcEntry <ydk.models.cisco_ios_xe.NHRP_MIB.NHRPMIB.NhrpServerNhcTable.NhrpServerNhcEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'NHRP-MIB'
        _revision = '1999-08-26'

        def __init__(self):
            super(NHRPMIB.NhrpServerNhcTable, self).__init__()

            self.yang_name = "nhrpServerNhcTable"
            self.yang_parent_name = "NHRP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("nhrpServerNhcEntry", ("nhrpservernhcentry", NHRPMIB.NhrpServerNhcTable.NhrpServerNhcEntry))])
            self._leafs = OrderedDict()

            self.nhrpservernhcentry = YList(self)
            self._segment_path = lambda: "nhrpServerNhcTable"
            self._absolute_path = lambda: "NHRP-MIB:NHRP-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(NHRPMIB.NhrpServerNhcTable, [], name, value)


        class NhrpServerNhcEntry(Entity):
            """
            An NHC that may be used by an NHS.
            
            .. attribute:: nhrpserverindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`nhrpserverindex <ydk.models.cisco_ios_xe.NHRP_MIB.NHRPMIB.NhrpServerTable.NhrpServerEntry>`
            
            	**config**\: False
            
            .. attribute:: nhrpservernhcindex  (key)
            
            	An identifier for an NHC available to an NHS
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpservernhcprefixlength
            
            	The number of bits that define the internetwork layer prefix associated with the nhrpServerNhcInternetworkAddr
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: nhrpservernhcinternetworkaddrtype
            
            	The type of the internetwork layer address of the NHRP Client represented in this entry. This object indicates how the value of nhrpServerNhcInternetworkAddr is to be interpreted
            	**type**\:  :py:class:`AddressFamilyNumbers <ydk.models.cisco_ios_xe.IANA_ADDRESS_FAMILY_NUMBERS_MIB.AddressFamilyNumbers>`
            
            	**config**\: False
            
            .. attribute:: nhrpservernhcinternetworkaddr
            
            	The value of the internetwork layer address of the NHRP Client represented by this entry.  If this value is not known, this will be a zero\-length OCTET STRING
            	**type**\: str
            
            	**length:** 0..64
            
            	**config**\: False
            
            .. attribute:: nhrpservernhcnbmaaddrtype
            
            	The type of the NBMA subnetwork address of the NHRP Client represented by this entry. This object indicates how the values of nhrpServerNhcNbmaAddr and nhrpServerNhcNbmaSubaddr are to be interpreted
            	**type**\:  :py:class:`AddressFamilyNumbers <ydk.models.cisco_ios_xe.IANA_ADDRESS_FAMILY_NUMBERS_MIB.AddressFamilyNumbers>`
            
            	**config**\: False
            
            .. attribute:: nhrpservernhcnbmaaddr
            
            	The NBMA subnetwork address of the NHC. The type of the address is indicated by the corresponding value of nhrpServerNbmaAddrType
            	**type**\: str
            
            	**length:** 0..64
            
            	**config**\: False
            
            .. attribute:: nhrpservernhcnbmasubaddr
            
            	The NBMA subaddress of the NHC. For NMBA address familes that do not have the concept of subaddress, this will be a zero\-length OCTET STRING
            	**type**\: str
            
            	**length:** 0..64
            
            	**config**\: False
            
            .. attribute:: nhrpservernhcinuse
            
            	An indication of whether this NHC is in use by the NHS
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: nhrpservernhcrowstatus
            
            	An object that allows entries in this table to be created and deleted using the RowStatus convention
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            

            """

            _prefix = 'NHRP-MIB'
            _revision = '1999-08-26'

            def __init__(self):
                super(NHRPMIB.NhrpServerNhcTable.NhrpServerNhcEntry, self).__init__()

                self.yang_name = "nhrpServerNhcEntry"
                self.yang_parent_name = "nhrpServerNhcTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['nhrpserverindex','nhrpservernhcindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('nhrpserverindex', (YLeaf(YType.str, 'nhrpServerIndex'), ['int'])),
                    ('nhrpservernhcindex', (YLeaf(YType.uint32, 'nhrpServerNhcIndex'), ['int'])),
                    ('nhrpservernhcprefixlength', (YLeaf(YType.int32, 'nhrpServerNhcPrefixLength'), ['int'])),
                    ('nhrpservernhcinternetworkaddrtype', (YLeaf(YType.enumeration, 'nhrpServerNhcInternetworkAddrType'), [('ydk.models.cisco_ios_xe.IANA_ADDRESS_FAMILY_NUMBERS_MIB', 'AddressFamilyNumbers', '')])),
                    ('nhrpservernhcinternetworkaddr', (YLeaf(YType.str, 'nhrpServerNhcInternetworkAddr'), ['str'])),
                    ('nhrpservernhcnbmaaddrtype', (YLeaf(YType.enumeration, 'nhrpServerNhcNbmaAddrType'), [('ydk.models.cisco_ios_xe.IANA_ADDRESS_FAMILY_NUMBERS_MIB', 'AddressFamilyNumbers', '')])),
                    ('nhrpservernhcnbmaaddr', (YLeaf(YType.str, 'nhrpServerNhcNbmaAddr'), ['str'])),
                    ('nhrpservernhcnbmasubaddr', (YLeaf(YType.str, 'nhrpServerNhcNbmaSubaddr'), ['str'])),
                    ('nhrpservernhcinuse', (YLeaf(YType.boolean, 'nhrpServerNhcInUse'), ['bool'])),
                    ('nhrpservernhcrowstatus', (YLeaf(YType.enumeration, 'nhrpServerNhcRowStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.nhrpserverindex = None
                self.nhrpservernhcindex = None
                self.nhrpservernhcprefixlength = None
                self.nhrpservernhcinternetworkaddrtype = None
                self.nhrpservernhcinternetworkaddr = None
                self.nhrpservernhcnbmaaddrtype = None
                self.nhrpservernhcnbmaaddr = None
                self.nhrpservernhcnbmasubaddr = None
                self.nhrpservernhcinuse = None
                self.nhrpservernhcrowstatus = None
                self._segment_path = lambda: "nhrpServerNhcEntry" + "[nhrpServerIndex='" + str(self.nhrpserverindex) + "']" + "[nhrpServerNhcIndex='" + str(self.nhrpservernhcindex) + "']"
                self._absolute_path = lambda: "NHRP-MIB:NHRP-MIB/nhrpServerNhcTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(NHRPMIB.NhrpServerNhcTable.NhrpServerNhcEntry, ['nhrpserverindex', 'nhrpservernhcindex', 'nhrpservernhcprefixlength', 'nhrpservernhcinternetworkaddrtype', 'nhrpservernhcinternetworkaddr', 'nhrpservernhcnbmaaddrtype', 'nhrpservernhcnbmaaddr', 'nhrpservernhcnbmasubaddr', 'nhrpservernhcinuse', 'nhrpservernhcrowstatus'], name, value)




    class NhrpServerStatTable(Entity):
        """
        Statistics collected by Next Hop Servers.
        
        .. attribute:: nhrpserverstatentry
        
        	Statistics for a particular NHS. The statistics are broken into received (Rx), transmitted (Tx) and forwarded (Fw).  Forwarded (Fw) would be done by a transit NHS
        	**type**\: list of  		 :py:class:`NhrpServerStatEntry <ydk.models.cisco_ios_xe.NHRP_MIB.NHRPMIB.NhrpServerStatTable.NhrpServerStatEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'NHRP-MIB'
        _revision = '1999-08-26'

        def __init__(self):
            super(NHRPMIB.NhrpServerStatTable, self).__init__()

            self.yang_name = "nhrpServerStatTable"
            self.yang_parent_name = "NHRP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("nhrpServerStatEntry", ("nhrpserverstatentry", NHRPMIB.NhrpServerStatTable.NhrpServerStatEntry))])
            self._leafs = OrderedDict()

            self.nhrpserverstatentry = YList(self)
            self._segment_path = lambda: "nhrpServerStatTable"
            self._absolute_path = lambda: "NHRP-MIB:NHRP-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(NHRPMIB.NhrpServerStatTable, [], name, value)


        class NhrpServerStatEntry(Entity):
            """
            Statistics for a particular NHS. The statistics are
            broken into received (Rx), transmitted (Tx)
            and forwarded (Fw).  Forwarded (Fw) would be done
            by a transit NHS.
            
            .. attribute:: nhrpserverindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`nhrpserverindex <ydk.models.cisco_ios_xe.NHRP_MIB.NHRPMIB.NhrpServerTable.NhrpServerEntry>`
            
            	**config**\: False
            
            .. attribute:: nhrpserverstatrxresolvereq
            
            	The number of NHRP Resolution Requests received by this server.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpserverstattxresolvereplyack
            
            	The number of positively acknowledged NHRP Resolution Replies transmitted by this server.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpserverstattxresolvereplynakprohibited
            
            	The number of NAKed NHRP Resolution Replies transmitted by this server with the code 'Administratively Prohibited'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpserverstattxresolvereplynakinsufresources
            
            	The number of NAKed NHRP Resolution Replies transmitted by this server with the code 'Insufficient Resources'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpserverstattxresolvereplynaknobinding
            
            	The number of NAKed NHRP Resolution Replies transmitted by this server with the code 'No Internetworking Layer Address to NBMA Address Binding Exists'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpserverstattxresolvereplynaknotunique
            
            	The number of NAKed NHRP Resolution Replies transmitted by this server with the code 'Binding Exists But Is Not Unique'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpserverstatrxregisterreq
            
            	The number of NHRP Registration Requests received by this server.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpserverstattxregisterack
            
            	The number of positively acknowledged NHRP Registration Replies transmitted by this server.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpserverstattxregisternakprohibited
            
            	The number of NAKed NHRP Registration Replies transmitted by this server with the code 'Administratively Prohibited'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpserverstattxregisternakinsufresources
            
            	The number of NAKed NHRP Registration Replies transmitted by this server with the code 'Insufficient Resources'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpserverstattxregisternakalreadyreg
            
            	The number of NAKed NHRP Registration Replies transmitted by this server with the code 'Unique Internetworking Layer Address Already Registered'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpserverstatrxpurgereq
            
            	The number of NHRP Purge Requests received by this server.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpserverstattxpurgereq
            
            	The number of NHRP Purge Requests transmitted by this server.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpserverstatrxpurgereply
            
            	The number of NHRP Purge Replies received by this server.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpserverstattxpurgereply
            
            	The number of NHRP Purge Replies transmitted by this server.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpserverstatrxerrunrecognizedextension
            
            	The number of NHRP Error Indication packets received by this server with the error code  'Unrecognized Extension'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpserverstatrxerrloopdetected
            
            	The number of NHRP Error Indication packets received by this server with the error code 'NHRP Loop Detected'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpserverstatrxerrprotoaddrunreachable
            
            	The number of NHRP Error Indication packets received by this server with the error code 'Protocol Address Unreachable'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpserverstatrxerrprotoerror
            
            	The number of NHRP Error Indication packets received by this server with the error code 'Protocol Error'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpserverstatrxerrsdusizeexceeded
            
            	The number of NHRP Error Indication packets received by this server with the error code 'NHRP SDU Size Exceeded'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpserverstatrxerrinvalidextension
            
            	The number of NHRP Error Indication packets received by this server with the error code 'Invalid Extension'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpserverstatrxerrinvalidresreplyreceived
            
            	The number of NHRP Error Indication packets received by this server with the error code 'Invalid Resolution Reply Received'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpserverstatrxerrauthenticationfailure
            
            	The number of NHRP Error Indication packets received by this server with the error code 'Authentication Failure'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpserverstatrxerrhopcountexceeded
            
            	The number of NHRP Error Indication packets received by this server with the error code 'Hop Count Exceeded'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpserverstattxerrunrecognizedextension
            
            	The number of NHRP Error Indication packets transmitted by this server with the error code 'Unrecognized Extension'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpserverstattxerrloopdetected
            
            	The number of NHRP Error Indication packets transmitted by this server with the error code 'NHRP Loop Detected'.     Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpserverstattxerrprotoaddrunreachable
            
            	The number of NHRP Error Indication packets transmitted by this server with the error code 'Protocol Address Unreachable'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpserverstattxerrprotoerror
            
            	The number of NHRP Error Indication packets transmitted by this server with the error code 'Protocol Error'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpserverstattxerrsdusizeexceeded
            
            	The number of NHRP Error Indication packets transmitted by this server with the error code 'NHRP SDU Size Exceeded'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpserverstattxerrinvalidextension
            
            	The number of NHRP Error Indication packets transmitted by this server with the error code  'Invalid Extension'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpserverstattxerrauthenticationfailure
            
            	The number of NHRP Error Indication packets transmitted by this server with the error code 'Authentication Failure'.     Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpserverstattxerrhopcountexceeded
            
            	The number of NHRP Error Indication packets transmitted by this server with the error code 'Hop Count Exceeded'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpserverstatfwresolvereq
            
            	The number of NHRP Resolution Requests forwarded by this server acting as a transit NHS.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpserverstatfwresolvereply
            
            	The number of NHRP Resolution Replies forwarded by this server acting as a transit NHS.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpserverstatfwregisterreq
            
            	The number of NHRP Registration Requests forwarded by this server acting as a transit NHS.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpserverstatfwregisterreply
            
            	The number of NHRP Registration Replies forwarded by this server acting as a transit NHS. Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpserverstatfwpurgereq
            
            	The number of NHRP Purge Requests forwarded by this server acting as a transit NHS.   Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpserverstatfwpurgereply
            
            	The number of NHRP Purge Replies forwarded by this server acting as a transit NHS.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpserverstatfwerrorindication
            
            	The number of NHRP Error Indication packets forwarded by this server acting as a transit NHS.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: nhrpserverstatdiscontinuitytime
            
            	The value of sysUpTime on the most recent occasion at which any one or more of this Server's counters suffered a discontinuity.  If no such discontinuities have occurred since the last re\-initialization of the    local management subsystem or the NHRP Server re\-initialization associated with this entry, then this object contains a zero value
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'NHRP-MIB'
            _revision = '1999-08-26'

            def __init__(self):
                super(NHRPMIB.NhrpServerStatTable.NhrpServerStatEntry, self).__init__()

                self.yang_name = "nhrpServerStatEntry"
                self.yang_parent_name = "nhrpServerStatTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['nhrpserverindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('nhrpserverindex', (YLeaf(YType.str, 'nhrpServerIndex'), ['int'])),
                    ('nhrpserverstatrxresolvereq', (YLeaf(YType.uint32, 'nhrpServerStatRxResolveReq'), ['int'])),
                    ('nhrpserverstattxresolvereplyack', (YLeaf(YType.uint32, 'nhrpServerStatTxResolveReplyAck'), ['int'])),
                    ('nhrpserverstattxresolvereplynakprohibited', (YLeaf(YType.uint32, 'nhrpServerStatTxResolveReplyNakProhibited'), ['int'])),
                    ('nhrpserverstattxresolvereplynakinsufresources', (YLeaf(YType.uint32, 'nhrpServerStatTxResolveReplyNakInsufResources'), ['int'])),
                    ('nhrpserverstattxresolvereplynaknobinding', (YLeaf(YType.uint32, 'nhrpServerStatTxResolveReplyNakNoBinding'), ['int'])),
                    ('nhrpserverstattxresolvereplynaknotunique', (YLeaf(YType.uint32, 'nhrpServerStatTxResolveReplyNakNotUnique'), ['int'])),
                    ('nhrpserverstatrxregisterreq', (YLeaf(YType.uint32, 'nhrpServerStatRxRegisterReq'), ['int'])),
                    ('nhrpserverstattxregisterack', (YLeaf(YType.uint32, 'nhrpServerStatTxRegisterAck'), ['int'])),
                    ('nhrpserverstattxregisternakprohibited', (YLeaf(YType.uint32, 'nhrpServerStatTxRegisterNakProhibited'), ['int'])),
                    ('nhrpserverstattxregisternakinsufresources', (YLeaf(YType.uint32, 'nhrpServerStatTxRegisterNakInsufResources'), ['int'])),
                    ('nhrpserverstattxregisternakalreadyreg', (YLeaf(YType.uint32, 'nhrpServerStatTxRegisterNakAlreadyReg'), ['int'])),
                    ('nhrpserverstatrxpurgereq', (YLeaf(YType.uint32, 'nhrpServerStatRxPurgeReq'), ['int'])),
                    ('nhrpserverstattxpurgereq', (YLeaf(YType.uint32, 'nhrpServerStatTxPurgeReq'), ['int'])),
                    ('nhrpserverstatrxpurgereply', (YLeaf(YType.uint32, 'nhrpServerStatRxPurgeReply'), ['int'])),
                    ('nhrpserverstattxpurgereply', (YLeaf(YType.uint32, 'nhrpServerStatTxPurgeReply'), ['int'])),
                    ('nhrpserverstatrxerrunrecognizedextension', (YLeaf(YType.uint32, 'nhrpServerStatRxErrUnrecognizedExtension'), ['int'])),
                    ('nhrpserverstatrxerrloopdetected', (YLeaf(YType.uint32, 'nhrpServerStatRxErrLoopDetected'), ['int'])),
                    ('nhrpserverstatrxerrprotoaddrunreachable', (YLeaf(YType.uint32, 'nhrpServerStatRxErrProtoAddrUnreachable'), ['int'])),
                    ('nhrpserverstatrxerrprotoerror', (YLeaf(YType.uint32, 'nhrpServerStatRxErrProtoError'), ['int'])),
                    ('nhrpserverstatrxerrsdusizeexceeded', (YLeaf(YType.uint32, 'nhrpServerStatRxErrSduSizeExceeded'), ['int'])),
                    ('nhrpserverstatrxerrinvalidextension', (YLeaf(YType.uint32, 'nhrpServerStatRxErrInvalidExtension'), ['int'])),
                    ('nhrpserverstatrxerrinvalidresreplyreceived', (YLeaf(YType.uint32, 'nhrpServerStatRxErrInvalidResReplyReceived'), ['int'])),
                    ('nhrpserverstatrxerrauthenticationfailure', (YLeaf(YType.uint32, 'nhrpServerStatRxErrAuthenticationFailure'), ['int'])),
                    ('nhrpserverstatrxerrhopcountexceeded', (YLeaf(YType.uint32, 'nhrpServerStatRxErrHopCountExceeded'), ['int'])),
                    ('nhrpserverstattxerrunrecognizedextension', (YLeaf(YType.uint32, 'nhrpServerStatTxErrUnrecognizedExtension'), ['int'])),
                    ('nhrpserverstattxerrloopdetected', (YLeaf(YType.uint32, 'nhrpServerStatTxErrLoopDetected'), ['int'])),
                    ('nhrpserverstattxerrprotoaddrunreachable', (YLeaf(YType.uint32, 'nhrpServerStatTxErrProtoAddrUnreachable'), ['int'])),
                    ('nhrpserverstattxerrprotoerror', (YLeaf(YType.uint32, 'nhrpServerStatTxErrProtoError'), ['int'])),
                    ('nhrpserverstattxerrsdusizeexceeded', (YLeaf(YType.uint32, 'nhrpServerStatTxErrSduSizeExceeded'), ['int'])),
                    ('nhrpserverstattxerrinvalidextension', (YLeaf(YType.uint32, 'nhrpServerStatTxErrInvalidExtension'), ['int'])),
                    ('nhrpserverstattxerrauthenticationfailure', (YLeaf(YType.uint32, 'nhrpServerStatTxErrAuthenticationFailure'), ['int'])),
                    ('nhrpserverstattxerrhopcountexceeded', (YLeaf(YType.uint32, 'nhrpServerStatTxErrHopCountExceeded'), ['int'])),
                    ('nhrpserverstatfwresolvereq', (YLeaf(YType.uint32, 'nhrpServerStatFwResolveReq'), ['int'])),
                    ('nhrpserverstatfwresolvereply', (YLeaf(YType.uint32, 'nhrpServerStatFwResolveReply'), ['int'])),
                    ('nhrpserverstatfwregisterreq', (YLeaf(YType.uint32, 'nhrpServerStatFwRegisterReq'), ['int'])),
                    ('nhrpserverstatfwregisterreply', (YLeaf(YType.uint32, 'nhrpServerStatFwRegisterReply'), ['int'])),
                    ('nhrpserverstatfwpurgereq', (YLeaf(YType.uint32, 'nhrpServerStatFwPurgeReq'), ['int'])),
                    ('nhrpserverstatfwpurgereply', (YLeaf(YType.uint32, 'nhrpServerStatFwPurgeReply'), ['int'])),
                    ('nhrpserverstatfwerrorindication', (YLeaf(YType.uint32, 'nhrpServerStatFwErrorIndication'), ['int'])),
                    ('nhrpserverstatdiscontinuitytime', (YLeaf(YType.uint32, 'nhrpServerStatDiscontinuityTime'), ['int'])),
                ])
                self.nhrpserverindex = None
                self.nhrpserverstatrxresolvereq = None
                self.nhrpserverstattxresolvereplyack = None
                self.nhrpserverstattxresolvereplynakprohibited = None
                self.nhrpserverstattxresolvereplynakinsufresources = None
                self.nhrpserverstattxresolvereplynaknobinding = None
                self.nhrpserverstattxresolvereplynaknotunique = None
                self.nhrpserverstatrxregisterreq = None
                self.nhrpserverstattxregisterack = None
                self.nhrpserverstattxregisternakprohibited = None
                self.nhrpserverstattxregisternakinsufresources = None
                self.nhrpserverstattxregisternakalreadyreg = None
                self.nhrpserverstatrxpurgereq = None
                self.nhrpserverstattxpurgereq = None
                self.nhrpserverstatrxpurgereply = None
                self.nhrpserverstattxpurgereply = None
                self.nhrpserverstatrxerrunrecognizedextension = None
                self.nhrpserverstatrxerrloopdetected = None
                self.nhrpserverstatrxerrprotoaddrunreachable = None
                self.nhrpserverstatrxerrprotoerror = None
                self.nhrpserverstatrxerrsdusizeexceeded = None
                self.nhrpserverstatrxerrinvalidextension = None
                self.nhrpserverstatrxerrinvalidresreplyreceived = None
                self.nhrpserverstatrxerrauthenticationfailure = None
                self.nhrpserverstatrxerrhopcountexceeded = None
                self.nhrpserverstattxerrunrecognizedextension = None
                self.nhrpserverstattxerrloopdetected = None
                self.nhrpserverstattxerrprotoaddrunreachable = None
                self.nhrpserverstattxerrprotoerror = None
                self.nhrpserverstattxerrsdusizeexceeded = None
                self.nhrpserverstattxerrinvalidextension = None
                self.nhrpserverstattxerrauthenticationfailure = None
                self.nhrpserverstattxerrhopcountexceeded = None
                self.nhrpserverstatfwresolvereq = None
                self.nhrpserverstatfwresolvereply = None
                self.nhrpserverstatfwregisterreq = None
                self.nhrpserverstatfwregisterreply = None
                self.nhrpserverstatfwpurgereq = None
                self.nhrpserverstatfwpurgereply = None
                self.nhrpserverstatfwerrorindication = None
                self.nhrpserverstatdiscontinuitytime = None
                self._segment_path = lambda: "nhrpServerStatEntry" + "[nhrpServerIndex='" + str(self.nhrpserverindex) + "']"
                self._absolute_path = lambda: "NHRP-MIB:NHRP-MIB/nhrpServerStatTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(NHRPMIB.NhrpServerStatTable.NhrpServerStatEntry, ['nhrpserverindex', 'nhrpserverstatrxresolvereq', 'nhrpserverstattxresolvereplyack', 'nhrpserverstattxresolvereplynakprohibited', 'nhrpserverstattxresolvereplynakinsufresources', 'nhrpserverstattxresolvereplynaknobinding', 'nhrpserverstattxresolvereplynaknotunique', 'nhrpserverstatrxregisterreq', 'nhrpserverstattxregisterack', 'nhrpserverstattxregisternakprohibited', 'nhrpserverstattxregisternakinsufresources', 'nhrpserverstattxregisternakalreadyreg', 'nhrpserverstatrxpurgereq', 'nhrpserverstattxpurgereq', 'nhrpserverstatrxpurgereply', 'nhrpserverstattxpurgereply', 'nhrpserverstatrxerrunrecognizedextension', 'nhrpserverstatrxerrloopdetected', 'nhrpserverstatrxerrprotoaddrunreachable', 'nhrpserverstatrxerrprotoerror', 'nhrpserverstatrxerrsdusizeexceeded', 'nhrpserverstatrxerrinvalidextension', 'nhrpserverstatrxerrinvalidresreplyreceived', 'nhrpserverstatrxerrauthenticationfailure', 'nhrpserverstatrxerrhopcountexceeded', 'nhrpserverstattxerrunrecognizedextension', 'nhrpserverstattxerrloopdetected', 'nhrpserverstattxerrprotoaddrunreachable', 'nhrpserverstattxerrprotoerror', 'nhrpserverstattxerrsdusizeexceeded', 'nhrpserverstattxerrinvalidextension', 'nhrpserverstattxerrauthenticationfailure', 'nhrpserverstattxerrhopcountexceeded', 'nhrpserverstatfwresolvereq', 'nhrpserverstatfwresolvereply', 'nhrpserverstatfwregisterreq', 'nhrpserverstatfwregisterreply', 'nhrpserverstatfwpurgereq', 'nhrpserverstatfwpurgereply', 'nhrpserverstatfwerrorindication', 'nhrpserverstatdiscontinuitytime'], name, value)



    def clone_ptr(self):
        self._top_entity = NHRPMIB()
        return self._top_entity



