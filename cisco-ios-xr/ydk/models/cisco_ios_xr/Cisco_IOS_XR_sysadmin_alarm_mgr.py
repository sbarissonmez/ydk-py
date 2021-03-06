""" Cisco_IOS_XR_sysadmin_alarm_mgr 

This module contains definitions
for the Calvados model objects.

This module contains a collection of YANG
definitions for Cisco IOS\-XR SysAdmin configuration.

Alarm management YANG model

Copyright(c) 2011\-2017 by Cisco Systems, Inc.
All rights reserved.

Copyright (c) 2012\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class AgentStateTd(Enum):
    """
    AgentStateTd (Enum Class)

    .. data:: start = 0

    .. data:: init = 1

    .. data:: connecting = 2

    .. data:: connected = 3

    .. data:: registered = 4

    .. data:: disconnected = 5

    """

    start = Enum.YLeaf(0, "start")

    init = Enum.YLeaf(1, "init")

    connecting = Enum.YLeaf(2, "connecting")

    connected = Enum.YLeaf(3, "connected")

    registered = Enum.YLeaf(4, "registered")

    disconnected = Enum.YLeaf(5, "disconnected")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_alarm_mgr as meta
        return meta._meta_table['AgentStateTd']


class AgentTypeTd(Enum):
    """
    AgentTypeTd (Enum Class)

    .. data:: unknown = 0

    .. data:: producer = 1

    .. data:: consumer = 2

    .. data:: subscriber = 3

    """

    unknown = Enum.YLeaf(0, "unknown")

    producer = Enum.YLeaf(1, "producer")

    consumer = Enum.YLeaf(2, "consumer")

    subscriber = Enum.YLeaf(3, "subscriber")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_alarm_mgr as meta
        return meta._meta_table['AgentTypeTd']


class GroupTd(Enum):
    """
    GroupTd (Enum Class)

    The group enumeration type of an alarm 

    .. data:: unknown = 0

    .. data:: environ = 1

    .. data:: ethernet = 2

    .. data:: fabric = 3

    .. data:: power = 4

    .. data:: software = 5

    .. data:: slice = 7

    .. data:: cpu = 8

    .. data:: controller = 9

    .. data:: sonet = 10

    .. data:: otn = 11

    .. data:: sdh_controller = 12

    .. data:: asic = 13

    .. data:: fpd_infra = 14

    .. data:: shelf = 15

    .. data:: mpa = 16

    .. data:: ots = 17

    .. data:: timing = 18

    .. data:: last = 19

    """

    unknown = Enum.YLeaf(0, "unknown")

    environ = Enum.YLeaf(1, "environ")

    ethernet = Enum.YLeaf(2, "ethernet")

    fabric = Enum.YLeaf(3, "fabric")

    power = Enum.YLeaf(4, "power")

    software = Enum.YLeaf(5, "software")

    slice = Enum.YLeaf(7, "slice")

    cpu = Enum.YLeaf(8, "cpu")

    controller = Enum.YLeaf(9, "controller")

    sonet = Enum.YLeaf(10, "sonet")

    otn = Enum.YLeaf(11, "otn")

    sdh_controller = Enum.YLeaf(12, "sdh_controller")

    asic = Enum.YLeaf(13, "asic")

    fpd_infra = Enum.YLeaf(14, "fpd_infra")

    shelf = Enum.YLeaf(15, "shelf")

    mpa = Enum.YLeaf(16, "mpa")

    ots = Enum.YLeaf(17, "ots")

    timing = Enum.YLeaf(18, "timing")

    last = Enum.YLeaf(19, "last")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_alarm_mgr as meta
        return meta._meta_table['GroupTd']


class SeverityTd(Enum):
    """
    SeverityTd (Enum Class)

    The severity enumeration type of an alarm 

    .. data:: unknown = 0

    .. data:: not_reported = 1

    .. data:: not_alarmed = 2

    .. data:: minor = 3

    .. data:: major = 4

    .. data:: critical = 5

    """

    unknown = Enum.YLeaf(0, "unknown")

    not_reported = Enum.YLeaf(1, "not_reported")

    not_alarmed = Enum.YLeaf(2, "not_alarmed")

    minor = Enum.YLeaf(3, "minor")

    major = Enum.YLeaf(4, "major")

    critical = Enum.YLeaf(5, "critical")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_alarm_mgr as meta
        return meta._meta_table['SeverityTd']


class StatusTd(Enum):
    """
    StatusTd (Enum Class)

    The status enumeration type of an alarm 

    .. data:: unknown = 0

    .. data:: set = 1

    .. data:: clear = 2

    .. data:: suppress = 3

    """

    unknown = Enum.YLeaf(0, "unknown")

    set = Enum.YLeaf(1, "set")

    clear = Enum.YLeaf(2, "clear")

    suppress = Enum.YLeaf(3, "suppress")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_alarm_mgr as meta
        return meta._meta_table['StatusTd']



class AlarmMgr(_Entity_):
    """
    Calvados alarms operational data model
    
    .. attribute:: trace
    
    	show traceable processes
    	**type**\: list of  		 :py:class:`Trace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.AlarmMgr.Trace>`
    
    	**config**\: False
    
    .. attribute:: brief
    
    	A set of brief alarm commands
    	**type**\:  :py:class:`Brief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.AlarmMgr.Brief>`
    
    	**config**\: False
    
    .. attribute:: detail
    
    	A set of detail alarm commands
    	**type**\:  :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.AlarmMgr.Detail>`
    
    	**config**\: False
    
    

    """

    _prefix = 'alarms'
    _revision = '2018-04-09'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(AlarmMgr, self).__init__()
        self._top_entity = None

        self.yang_name = "alarm_mgr"
        self.yang_parent_name = "Cisco-IOS-XR-sysadmin-alarm-mgr"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("trace", ("trace", AlarmMgr.Trace)), ("brief", ("brief", AlarmMgr.Brief)), ("detail", ("detail", AlarmMgr.Detail))])
        self._leafs = OrderedDict()

        self.brief = AlarmMgr.Brief()
        self.brief.parent = self
        self._children_name_map["brief"] = "brief"

        self.detail = AlarmMgr.Detail()
        self.detail.parent = self
        self._children_name_map["detail"] = "detail"

        self.trace = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-alarm-mgr:alarm_mgr"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(AlarmMgr, [], name, value)


    class Trace(_Entity_):
        """
        show traceable processes
        
        .. attribute:: buffer  (key)
        
        	
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: location
        
        	
        	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.AlarmMgr.Trace.Location>`
        
        	**config**\: False
        
        

        """

        _prefix = 'alarms'
        _revision = '2018-04-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(AlarmMgr.Trace, self).__init__()

            self.yang_name = "trace"
            self.yang_parent_name = "alarm_mgr"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['buffer']
            self._child_classes = OrderedDict([("location", ("location", AlarmMgr.Trace.Location))])
            self._leafs = OrderedDict([
                ('buffer', (YLeaf(YType.str, 'buffer'), ['str'])),
            ])
            self.buffer = None

            self.location = YList(self)
            self._segment_path = lambda: "trace" + "[buffer='" + str(self.buffer) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-alarm-mgr:alarm_mgr/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(AlarmMgr.Trace, ['buffer'], name, value)


        class Location(_Entity_):
            """
            
            
            .. attribute:: location_name  (key)
            
            	
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: all_options
            
            	
            	**type**\: list of  		 :py:class:`AllOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.AlarmMgr.Trace.Location.AllOptions>`
            
            	**config**\: False
            
            

            """

            _prefix = 'alarms'
            _revision = '2018-04-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(AlarmMgr.Trace.Location, self).__init__()

                self.yang_name = "location"
                self.yang_parent_name = "trace"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = ['location_name']
                self._child_classes = OrderedDict([("all-options", ("all_options", AlarmMgr.Trace.Location.AllOptions))])
                self._leafs = OrderedDict([
                    ('location_name', (YLeaf(YType.str, 'location_name'), ['str'])),
                ])
                self.location_name = None

                self.all_options = YList(self)
                self._segment_path = lambda: "location" + "[location_name='" + str(self.location_name) + "']"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(AlarmMgr.Trace.Location, ['location_name'], name, value)


            class AllOptions(_Entity_):
                """
                
                
                .. attribute:: option  (key)
                
                	
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: trace_blocks
                
                	
                	**type**\: list of  		 :py:class:`TraceBlocks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.AlarmMgr.Trace.Location.AllOptions.TraceBlocks>`
                
                	**config**\: False
                
                

                """

                _prefix = 'alarms'
                _revision = '2018-04-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(AlarmMgr.Trace.Location.AllOptions, self).__init__()

                    self.yang_name = "all-options"
                    self.yang_parent_name = "location"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['option']
                    self._child_classes = OrderedDict([("trace-blocks", ("trace_blocks", AlarmMgr.Trace.Location.AllOptions.TraceBlocks))])
                    self._leafs = OrderedDict([
                        ('option', (YLeaf(YType.str, 'option'), ['str'])),
                    ])
                    self.option = None

                    self.trace_blocks = YList(self)
                    self._segment_path = lambda: "all-options" + "[option='" + str(self.option) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AlarmMgr.Trace.Location.AllOptions, ['option'], name, value)


                class TraceBlocks(_Entity_):
                    """
                    
                    
                    .. attribute:: data
                    
                    	Trace output block
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'alarms'
                    _revision = '2018-04-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(AlarmMgr.Trace.Location.AllOptions.TraceBlocks, self).__init__()

                        self.yang_name = "trace-blocks"
                        self.yang_parent_name = "all-options"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('data', (YLeaf(YType.str, 'data'), ['str'])),
                        ])
                        self.data = None
                        self._segment_path = lambda: "trace-blocks"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AlarmMgr.Trace.Location.AllOptions.TraceBlocks, ['data'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_alarm_mgr as meta
                        return meta._meta_table['AlarmMgr.Trace.Location.AllOptions.TraceBlocks']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_alarm_mgr as meta
                    return meta._meta_table['AlarmMgr.Trace.Location.AllOptions']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_alarm_mgr as meta
                return meta._meta_table['AlarmMgr.Trace.Location']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_alarm_mgr as meta
            return meta._meta_table['AlarmMgr.Trace']['meta_info']


    class Brief(_Entity_):
        """
        A set of brief alarm commands
        
        .. attribute:: card
        
        	Alarms reported at the local card as specified by the location parameter
        	**type**\:  :py:class:`Card <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.AlarmMgr.Brief.Card>`
        
        	**config**\: False
        
        .. attribute:: rack
        
        	Alarms reported at the rack scope specified by the rack\-id
        	**type**\:  :py:class:`Rack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.AlarmMgr.Brief.Rack>`
        
        	**config**\: False
        
        .. attribute:: system
        
        	Alarms reported at the system scope
        	**type**\:  :py:class:`System <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.AlarmMgr.Brief.System>`
        
        	**config**\: False
        
        

        """

        _prefix = 'alarms'
        _revision = '2018-04-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(AlarmMgr.Brief, self).__init__()

            self.yang_name = "brief"
            self.yang_parent_name = "alarm_mgr"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("card", ("card", AlarmMgr.Brief.Card)), ("rack", ("rack", AlarmMgr.Brief.Rack)), ("system", ("system", AlarmMgr.Brief.System))])
            self._leafs = OrderedDict()

            self.card = AlarmMgr.Brief.Card()
            self.card.parent = self
            self._children_name_map["card"] = "card"

            self.rack = AlarmMgr.Brief.Rack()
            self.rack.parent = self
            self._children_name_map["rack"] = "rack"

            self.system = AlarmMgr.Brief.System()
            self.system.parent = self
            self._children_name_map["system"] = "system"
            self._segment_path = lambda: "brief"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-alarm-mgr:alarm_mgr/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(AlarmMgr.Brief, [], name, value)


        class Card(_Entity_):
            """
            Alarms reported at the local card as
            specified by the location parameter
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.AlarmMgr.Brief.Card.Location>`
            
            	**config**\: False
            
            

            """

            _prefix = 'alarms'
            _revision = '2018-04-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(AlarmMgr.Brief.Card, self).__init__()

                self.yang_name = "card"
                self.yang_parent_name = "brief"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("location", ("location", AlarmMgr.Brief.Card.Location))])
                self._leafs = OrderedDict()

                self.location = YList(self)
                self._segment_path = lambda: "card"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-alarm-mgr:alarm_mgr/brief/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(AlarmMgr.Brief.Card, [], name, value)


            class Location(_Entity_):
                """
                
                
                .. attribute:: locations  (key)
                
                	
                	**type**\: str
                
                	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                
                	**config**\: False
                
                .. attribute:: active
                
                	
                	**type**\: list of  		 :py:class:`Active <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.AlarmMgr.Brief.Card.Location.Active>`
                
                	**config**\: False
                
                .. attribute:: history
                
                	
                	**type**\: list of  		 :py:class:`History <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.AlarmMgr.Brief.Card.Location.History>`
                
                	**config**\: False
                
                .. attribute:: suppressed
                
                	
                	**type**\: list of  		 :py:class:`Suppressed <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.AlarmMgr.Brief.Card.Location.Suppressed>`
                
                	**config**\: False
                
                

                """

                _prefix = 'alarms'
                _revision = '2018-04-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(AlarmMgr.Brief.Card.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "card"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['locations']
                    self._child_classes = OrderedDict([("active", ("active", AlarmMgr.Brief.Card.Location.Active)), ("history", ("history", AlarmMgr.Brief.Card.Location.History)), ("suppressed", ("suppressed", AlarmMgr.Brief.Card.Location.Suppressed))])
                    self._leafs = OrderedDict([
                        ('locations', (YLeaf(YType.str, 'locations'), ['str'])),
                    ])
                    self.locations = None

                    self.active = YList(self)
                    self.history = YList(self)
                    self.suppressed = YList(self)
                    self._segment_path = lambda: "location" + "[locations='" + str(self.locations) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-alarm-mgr:alarm_mgr/brief/card/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AlarmMgr.Brief.Card.Location, ['locations'], name, value)


                class Active(_Entity_):
                    """
                    
                    
                    .. attribute:: aid  (key)
                    
                    	The AID for the current alarm
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: eid  (key)
                    
                    	The Object Id for the current alarm
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: tag
                    
                    	The Fault Tag for the current alarm
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: module
                    
                    	The Module for the current alarm
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: gen_location
                    
                    	The location for the current alarm
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: severity
                    
                    	The alarm severity
                    	**type**\:  :py:class:`SeverityTd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.SeverityTd>`
                    
                    	**config**\: False
                    
                    .. attribute:: group
                    
                    	The alarm grouping 
                    	**type**\:  :py:class:`GroupTd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.GroupTd>`
                    
                    	**config**\: False
                    
                    .. attribute:: description
                    
                    	Alarm description
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: set_time
                    
                    	Alarm set time stamp
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'alarms'
                    _revision = '2018-04-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(AlarmMgr.Brief.Card.Location.Active, self).__init__()

                        self.yang_name = "active"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['aid','eid']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('aid', (YLeaf(YType.str, 'aid'), ['str'])),
                            ('eid', (YLeaf(YType.str, 'eid'), ['str'])),
                            ('tag', (YLeaf(YType.str, 'tag'), ['str'])),
                            ('module', (YLeaf(YType.str, 'module'), ['str'])),
                            ('gen_location', (YLeaf(YType.str, 'gen_location'), ['str'])),
                            ('severity', (YLeaf(YType.enumeration, 'severity'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr', 'SeverityTd', '')])),
                            ('group', (YLeaf(YType.enumeration, 'group'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr', 'GroupTd', '')])),
                            ('description', (YLeaf(YType.str, 'description'), ['str'])),
                            ('set_time', (YLeaf(YType.str, 'set_time'), ['str'])),
                        ])
                        self.aid = None
                        self.eid = None
                        self.tag = None
                        self.module = None
                        self.gen_location = None
                        self.severity = None
                        self.group = None
                        self.description = None
                        self.set_time = None
                        self._segment_path = lambda: "active" + "[aid='" + str(self.aid) + "']" + "[eid='" + str(self.eid) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AlarmMgr.Brief.Card.Location.Active, ['aid', 'eid', 'tag', 'module', 'gen_location', 'severity', 'group', 'description', 'set_time'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_alarm_mgr as meta
                        return meta._meta_table['AlarmMgr.Brief.Card.Location.Active']['meta_info']


                class History(_Entity_):
                    """
                    
                    
                    .. attribute:: aid  (key)
                    
                    	The AID for the current alarm
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: eid  (key)
                    
                    	The Object Id for the current alarm
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: tag
                    
                    	The Fault Tag for the current alarm
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: module
                    
                    	The Module for the current alarm
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: gen_location
                    
                    	The location for the current alarm
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: severity
                    
                    	The alarm severity
                    	**type**\:  :py:class:`SeverityTd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.SeverityTd>`
                    
                    	**config**\: False
                    
                    .. attribute:: group
                    
                    	The alarm grouping 
                    	**type**\:  :py:class:`GroupTd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.GroupTd>`
                    
                    	**config**\: False
                    
                    .. attribute:: description
                    
                    	Alarm description
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: set_time
                    
                    	Alarm set time stamp
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: clear_time
                    
                    	Alarm clear time stamp
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'alarms'
                    _revision = '2018-04-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(AlarmMgr.Brief.Card.Location.History, self).__init__()

                        self.yang_name = "history"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['aid','eid']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('aid', (YLeaf(YType.str, 'aid'), ['str'])),
                            ('eid', (YLeaf(YType.str, 'eid'), ['str'])),
                            ('tag', (YLeaf(YType.str, 'tag'), ['str'])),
                            ('module', (YLeaf(YType.str, 'module'), ['str'])),
                            ('gen_location', (YLeaf(YType.str, 'gen_location'), ['str'])),
                            ('severity', (YLeaf(YType.enumeration, 'severity'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr', 'SeverityTd', '')])),
                            ('group', (YLeaf(YType.enumeration, 'group'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr', 'GroupTd', '')])),
                            ('description', (YLeaf(YType.str, 'description'), ['str'])),
                            ('set_time', (YLeaf(YType.str, 'set_time'), ['str'])),
                            ('clear_time', (YLeaf(YType.str, 'clear_time'), ['str'])),
                        ])
                        self.aid = None
                        self.eid = None
                        self.tag = None
                        self.module = None
                        self.gen_location = None
                        self.severity = None
                        self.group = None
                        self.description = None
                        self.set_time = None
                        self.clear_time = None
                        self._segment_path = lambda: "history" + "[aid='" + str(self.aid) + "']" + "[eid='" + str(self.eid) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AlarmMgr.Brief.Card.Location.History, ['aid', 'eid', 'tag', 'module', 'gen_location', 'severity', 'group', 'description', 'set_time', 'clear_time'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_alarm_mgr as meta
                        return meta._meta_table['AlarmMgr.Brief.Card.Location.History']['meta_info']


                class Suppressed(_Entity_):
                    """
                    
                    
                    .. attribute:: aid  (key)
                    
                    	The AID for the current alarm
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: eid  (key)
                    
                    	The Object Id for the current alarm
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: tag
                    
                    	The Fault Tag for the current alarm
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: module
                    
                    	The Module for the current alarm
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: gen_location
                    
                    	The location for the current alarm
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: severity
                    
                    	The alarm severity
                    	**type**\:  :py:class:`SeverityTd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.SeverityTd>`
                    
                    	**config**\: False
                    
                    .. attribute:: group
                    
                    	The alarm grouping 
                    	**type**\:  :py:class:`GroupTd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.GroupTd>`
                    
                    	**config**\: False
                    
                    .. attribute:: description
                    
                    	Alarm description
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: set_time
                    
                    	Alarm set time stamp
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: suppressed_time
                    
                    	Alarm suppressed time stamp
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'alarms'
                    _revision = '2018-04-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(AlarmMgr.Brief.Card.Location.Suppressed, self).__init__()

                        self.yang_name = "suppressed"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['aid','eid']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('aid', (YLeaf(YType.str, 'aid'), ['str'])),
                            ('eid', (YLeaf(YType.str, 'eid'), ['str'])),
                            ('tag', (YLeaf(YType.str, 'tag'), ['str'])),
                            ('module', (YLeaf(YType.str, 'module'), ['str'])),
                            ('gen_location', (YLeaf(YType.str, 'gen_location'), ['str'])),
                            ('severity', (YLeaf(YType.enumeration, 'severity'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr', 'SeverityTd', '')])),
                            ('group', (YLeaf(YType.enumeration, 'group'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr', 'GroupTd', '')])),
                            ('description', (YLeaf(YType.str, 'description'), ['str'])),
                            ('set_time', (YLeaf(YType.str, 'set_time'), ['str'])),
                            ('suppressed_time', (YLeaf(YType.str, 'suppressed_time'), ['str'])),
                        ])
                        self.aid = None
                        self.eid = None
                        self.tag = None
                        self.module = None
                        self.gen_location = None
                        self.severity = None
                        self.group = None
                        self.description = None
                        self.set_time = None
                        self.suppressed_time = None
                        self._segment_path = lambda: "suppressed" + "[aid='" + str(self.aid) + "']" + "[eid='" + str(self.eid) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AlarmMgr.Brief.Card.Location.Suppressed, ['aid', 'eid', 'tag', 'module', 'gen_location', 'severity', 'group', 'description', 'set_time', 'suppressed_time'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_alarm_mgr as meta
                        return meta._meta_table['AlarmMgr.Brief.Card.Location.Suppressed']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_alarm_mgr as meta
                    return meta._meta_table['AlarmMgr.Brief.Card.Location']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_alarm_mgr as meta
                return meta._meta_table['AlarmMgr.Brief.Card']['meta_info']


        class Rack(_Entity_):
            """
            Alarms reported at the rack scope
            specified by the rack\-id
            
            .. attribute:: rack_locations
            
            	
            	**type**\: list of  		 :py:class:`RackLocations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.AlarmMgr.Brief.Rack.RackLocations>`
            
            	**config**\: False
            
            

            """

            _prefix = 'alarms'
            _revision = '2018-04-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(AlarmMgr.Brief.Rack, self).__init__()

                self.yang_name = "rack"
                self.yang_parent_name = "brief"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("rack_locations", ("rack_locations", AlarmMgr.Brief.Rack.RackLocations))])
                self._leafs = OrderedDict()

                self.rack_locations = YList(self)
                self._segment_path = lambda: "rack"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-alarm-mgr:alarm_mgr/brief/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(AlarmMgr.Brief.Rack, [], name, value)


            class RackLocations(_Entity_):
                """
                
                
                .. attribute:: rackid  (key)
                
                	
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: active
                
                	
                	**type**\: list of  		 :py:class:`Active <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.AlarmMgr.Brief.Rack.RackLocations.Active>`
                
                	**config**\: False
                
                .. attribute:: history
                
                	
                	**type**\: list of  		 :py:class:`History <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.AlarmMgr.Brief.Rack.RackLocations.History>`
                
                	**config**\: False
                
                .. attribute:: suppressed
                
                	
                	**type**\: list of  		 :py:class:`Suppressed <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.AlarmMgr.Brief.Rack.RackLocations.Suppressed>`
                
                	**config**\: False
                
                

                """

                _prefix = 'alarms'
                _revision = '2018-04-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(AlarmMgr.Brief.Rack.RackLocations, self).__init__()

                    self.yang_name = "rack_locations"
                    self.yang_parent_name = "rack"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['rackid']
                    self._child_classes = OrderedDict([("active", ("active", AlarmMgr.Brief.Rack.RackLocations.Active)), ("history", ("history", AlarmMgr.Brief.Rack.RackLocations.History)), ("suppressed", ("suppressed", AlarmMgr.Brief.Rack.RackLocations.Suppressed))])
                    self._leafs = OrderedDict([
                        ('rackid', (YLeaf(YType.uint32, 'rackid'), ['int'])),
                    ])
                    self.rackid = None

                    self.active = YList(self)
                    self.history = YList(self)
                    self.suppressed = YList(self)
                    self._segment_path = lambda: "rack_locations" + "[rackid='" + str(self.rackid) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-alarm-mgr:alarm_mgr/brief/rack/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AlarmMgr.Brief.Rack.RackLocations, ['rackid'], name, value)


                class Active(_Entity_):
                    """
                    
                    
                    .. attribute:: aid  (key)
                    
                    	The AID for the current alarm
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: eid  (key)
                    
                    	The Object Id for the current alarm
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: tag
                    
                    	The Fault Tag for the current alarm
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: module
                    
                    	The Module for the current alarm
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: gen_location
                    
                    	The location for the current alarm
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: severity
                    
                    	The alarm severity
                    	**type**\:  :py:class:`SeverityTd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.SeverityTd>`
                    
                    	**config**\: False
                    
                    .. attribute:: group
                    
                    	The alarm grouping 
                    	**type**\:  :py:class:`GroupTd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.GroupTd>`
                    
                    	**config**\: False
                    
                    .. attribute:: description
                    
                    	Alarm description
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: set_time
                    
                    	Alarm set time stamp
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'alarms'
                    _revision = '2018-04-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(AlarmMgr.Brief.Rack.RackLocations.Active, self).__init__()

                        self.yang_name = "active"
                        self.yang_parent_name = "rack_locations"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['aid','eid']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('aid', (YLeaf(YType.str, 'aid'), ['str'])),
                            ('eid', (YLeaf(YType.str, 'eid'), ['str'])),
                            ('tag', (YLeaf(YType.str, 'tag'), ['str'])),
                            ('module', (YLeaf(YType.str, 'module'), ['str'])),
                            ('gen_location', (YLeaf(YType.str, 'gen_location'), ['str'])),
                            ('severity', (YLeaf(YType.enumeration, 'severity'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr', 'SeverityTd', '')])),
                            ('group', (YLeaf(YType.enumeration, 'group'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr', 'GroupTd', '')])),
                            ('description', (YLeaf(YType.str, 'description'), ['str'])),
                            ('set_time', (YLeaf(YType.str, 'set_time'), ['str'])),
                        ])
                        self.aid = None
                        self.eid = None
                        self.tag = None
                        self.module = None
                        self.gen_location = None
                        self.severity = None
                        self.group = None
                        self.description = None
                        self.set_time = None
                        self._segment_path = lambda: "active" + "[aid='" + str(self.aid) + "']" + "[eid='" + str(self.eid) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AlarmMgr.Brief.Rack.RackLocations.Active, ['aid', 'eid', 'tag', 'module', 'gen_location', 'severity', 'group', 'description', 'set_time'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_alarm_mgr as meta
                        return meta._meta_table['AlarmMgr.Brief.Rack.RackLocations.Active']['meta_info']


                class History(_Entity_):
                    """
                    
                    
                    .. attribute:: aid  (key)
                    
                    	The AID for the current alarm
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: eid  (key)
                    
                    	The Object Id for the current alarm
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: tag
                    
                    	The Fault Tag for the current alarm
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: module
                    
                    	The Module for the current alarm
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: gen_location
                    
                    	The location for the current alarm
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: severity
                    
                    	The alarm severity
                    	**type**\:  :py:class:`SeverityTd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.SeverityTd>`
                    
                    	**config**\: False
                    
                    .. attribute:: group
                    
                    	The alarm grouping 
                    	**type**\:  :py:class:`GroupTd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.GroupTd>`
                    
                    	**config**\: False
                    
                    .. attribute:: description
                    
                    	Alarm description
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: set_time
                    
                    	Alarm set time stamp
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: clear_time
                    
                    	Alarm clear time stamp
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'alarms'
                    _revision = '2018-04-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(AlarmMgr.Brief.Rack.RackLocations.History, self).__init__()

                        self.yang_name = "history"
                        self.yang_parent_name = "rack_locations"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['aid','eid']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('aid', (YLeaf(YType.str, 'aid'), ['str'])),
                            ('eid', (YLeaf(YType.str, 'eid'), ['str'])),
                            ('tag', (YLeaf(YType.str, 'tag'), ['str'])),
                            ('module', (YLeaf(YType.str, 'module'), ['str'])),
                            ('gen_location', (YLeaf(YType.str, 'gen_location'), ['str'])),
                            ('severity', (YLeaf(YType.enumeration, 'severity'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr', 'SeverityTd', '')])),
                            ('group', (YLeaf(YType.enumeration, 'group'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr', 'GroupTd', '')])),
                            ('description', (YLeaf(YType.str, 'description'), ['str'])),
                            ('set_time', (YLeaf(YType.str, 'set_time'), ['str'])),
                            ('clear_time', (YLeaf(YType.str, 'clear_time'), ['str'])),
                        ])
                        self.aid = None
                        self.eid = None
                        self.tag = None
                        self.module = None
                        self.gen_location = None
                        self.severity = None
                        self.group = None
                        self.description = None
                        self.set_time = None
                        self.clear_time = None
                        self._segment_path = lambda: "history" + "[aid='" + str(self.aid) + "']" + "[eid='" + str(self.eid) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AlarmMgr.Brief.Rack.RackLocations.History, ['aid', 'eid', 'tag', 'module', 'gen_location', 'severity', 'group', 'description', 'set_time', 'clear_time'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_alarm_mgr as meta
                        return meta._meta_table['AlarmMgr.Brief.Rack.RackLocations.History']['meta_info']


                class Suppressed(_Entity_):
                    """
                    
                    
                    .. attribute:: aid  (key)
                    
                    	The AID for the current alarm
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: eid  (key)
                    
                    	The Object Id for the current alarm
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: tag
                    
                    	The Fault Tag for the current alarm
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: module
                    
                    	The Module for the current alarm
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: gen_location
                    
                    	The location for the current alarm
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: severity
                    
                    	The alarm severity
                    	**type**\:  :py:class:`SeverityTd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.SeverityTd>`
                    
                    	**config**\: False
                    
                    .. attribute:: group
                    
                    	The alarm grouping 
                    	**type**\:  :py:class:`GroupTd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.GroupTd>`
                    
                    	**config**\: False
                    
                    .. attribute:: description
                    
                    	Alarm description
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: set_time
                    
                    	Alarm set time stamp
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: suppressed_time
                    
                    	Alarm suppressed time stamp
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'alarms'
                    _revision = '2018-04-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(AlarmMgr.Brief.Rack.RackLocations.Suppressed, self).__init__()

                        self.yang_name = "suppressed"
                        self.yang_parent_name = "rack_locations"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['aid','eid']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('aid', (YLeaf(YType.str, 'aid'), ['str'])),
                            ('eid', (YLeaf(YType.str, 'eid'), ['str'])),
                            ('tag', (YLeaf(YType.str, 'tag'), ['str'])),
                            ('module', (YLeaf(YType.str, 'module'), ['str'])),
                            ('gen_location', (YLeaf(YType.str, 'gen_location'), ['str'])),
                            ('severity', (YLeaf(YType.enumeration, 'severity'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr', 'SeverityTd', '')])),
                            ('group', (YLeaf(YType.enumeration, 'group'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr', 'GroupTd', '')])),
                            ('description', (YLeaf(YType.str, 'description'), ['str'])),
                            ('set_time', (YLeaf(YType.str, 'set_time'), ['str'])),
                            ('suppressed_time', (YLeaf(YType.str, 'suppressed_time'), ['str'])),
                        ])
                        self.aid = None
                        self.eid = None
                        self.tag = None
                        self.module = None
                        self.gen_location = None
                        self.severity = None
                        self.group = None
                        self.description = None
                        self.set_time = None
                        self.suppressed_time = None
                        self._segment_path = lambda: "suppressed" + "[aid='" + str(self.aid) + "']" + "[eid='" + str(self.eid) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AlarmMgr.Brief.Rack.RackLocations.Suppressed, ['aid', 'eid', 'tag', 'module', 'gen_location', 'severity', 'group', 'description', 'set_time', 'suppressed_time'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_alarm_mgr as meta
                        return meta._meta_table['AlarmMgr.Brief.Rack.RackLocations.Suppressed']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_alarm_mgr as meta
                    return meta._meta_table['AlarmMgr.Brief.Rack.RackLocations']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_alarm_mgr as meta
                return meta._meta_table['AlarmMgr.Brief.Rack']['meta_info']


        class System(_Entity_):
            """
            Alarms reported at the system scope
            
            .. attribute:: active
            
            	
            	**type**\: list of  		 :py:class:`Active <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.AlarmMgr.Brief.System.Active>`
            
            	**config**\: False
            
            .. attribute:: history
            
            	
            	**type**\: list of  		 :py:class:`History <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.AlarmMgr.Brief.System.History>`
            
            	**config**\: False
            
            .. attribute:: suppressed
            
            	
            	**type**\: list of  		 :py:class:`Suppressed <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.AlarmMgr.Brief.System.Suppressed>`
            
            	**config**\: False
            
            

            """

            _prefix = 'alarms'
            _revision = '2018-04-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(AlarmMgr.Brief.System, self).__init__()

                self.yang_name = "system"
                self.yang_parent_name = "brief"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("active", ("active", AlarmMgr.Brief.System.Active)), ("history", ("history", AlarmMgr.Brief.System.History)), ("suppressed", ("suppressed", AlarmMgr.Brief.System.Suppressed))])
                self._leafs = OrderedDict()

                self.active = YList(self)
                self.history = YList(self)
                self.suppressed = YList(self)
                self._segment_path = lambda: "system"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-alarm-mgr:alarm_mgr/brief/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(AlarmMgr.Brief.System, [], name, value)


            class Active(_Entity_):
                """
                
                
                .. attribute:: aid  (key)
                
                	The AID for the current alarm
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: eid  (key)
                
                	The Object Id for the current alarm
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: tag
                
                	The Fault Tag for the current alarm
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: module
                
                	The Module for the current alarm
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: gen_location
                
                	The location for the current alarm
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: severity
                
                	The alarm severity
                	**type**\:  :py:class:`SeverityTd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.SeverityTd>`
                
                	**config**\: False
                
                .. attribute:: group
                
                	The alarm grouping 
                	**type**\:  :py:class:`GroupTd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.GroupTd>`
                
                	**config**\: False
                
                .. attribute:: description
                
                	Alarm description
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: set_time
                
                	Alarm set time stamp
                	**type**\: str
                
                	**config**\: False
                
                

                """

                _prefix = 'alarms'
                _revision = '2018-04-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(AlarmMgr.Brief.System.Active, self).__init__()

                    self.yang_name = "active"
                    self.yang_parent_name = "system"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['aid','eid']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('aid', (YLeaf(YType.str, 'aid'), ['str'])),
                        ('eid', (YLeaf(YType.str, 'eid'), ['str'])),
                        ('tag', (YLeaf(YType.str, 'tag'), ['str'])),
                        ('module', (YLeaf(YType.str, 'module'), ['str'])),
                        ('gen_location', (YLeaf(YType.str, 'gen_location'), ['str'])),
                        ('severity', (YLeaf(YType.enumeration, 'severity'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr', 'SeverityTd', '')])),
                        ('group', (YLeaf(YType.enumeration, 'group'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr', 'GroupTd', '')])),
                        ('description', (YLeaf(YType.str, 'description'), ['str'])),
                        ('set_time', (YLeaf(YType.str, 'set_time'), ['str'])),
                    ])
                    self.aid = None
                    self.eid = None
                    self.tag = None
                    self.module = None
                    self.gen_location = None
                    self.severity = None
                    self.group = None
                    self.description = None
                    self.set_time = None
                    self._segment_path = lambda: "active" + "[aid='" + str(self.aid) + "']" + "[eid='" + str(self.eid) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-alarm-mgr:alarm_mgr/brief/system/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AlarmMgr.Brief.System.Active, ['aid', 'eid', 'tag', 'module', 'gen_location', 'severity', 'group', 'description', 'set_time'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_alarm_mgr as meta
                    return meta._meta_table['AlarmMgr.Brief.System.Active']['meta_info']


            class History(_Entity_):
                """
                
                
                .. attribute:: aid  (key)
                
                	The AID for the current alarm
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: eid  (key)
                
                	The Object Id for the current alarm
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: tag
                
                	The Fault Tag for the current alarm
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: module
                
                	The Module for the current alarm
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: gen_location
                
                	The location for the current alarm
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: severity
                
                	The alarm severity
                	**type**\:  :py:class:`SeverityTd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.SeverityTd>`
                
                	**config**\: False
                
                .. attribute:: group
                
                	The alarm grouping 
                	**type**\:  :py:class:`GroupTd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.GroupTd>`
                
                	**config**\: False
                
                .. attribute:: description
                
                	Alarm description
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: set_time
                
                	Alarm set time stamp
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: clear_time
                
                	Alarm clear time stamp
                	**type**\: str
                
                	**config**\: False
                
                

                """

                _prefix = 'alarms'
                _revision = '2018-04-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(AlarmMgr.Brief.System.History, self).__init__()

                    self.yang_name = "history"
                    self.yang_parent_name = "system"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['aid','eid']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('aid', (YLeaf(YType.str, 'aid'), ['str'])),
                        ('eid', (YLeaf(YType.str, 'eid'), ['str'])),
                        ('tag', (YLeaf(YType.str, 'tag'), ['str'])),
                        ('module', (YLeaf(YType.str, 'module'), ['str'])),
                        ('gen_location', (YLeaf(YType.str, 'gen_location'), ['str'])),
                        ('severity', (YLeaf(YType.enumeration, 'severity'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr', 'SeverityTd', '')])),
                        ('group', (YLeaf(YType.enumeration, 'group'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr', 'GroupTd', '')])),
                        ('description', (YLeaf(YType.str, 'description'), ['str'])),
                        ('set_time', (YLeaf(YType.str, 'set_time'), ['str'])),
                        ('clear_time', (YLeaf(YType.str, 'clear_time'), ['str'])),
                    ])
                    self.aid = None
                    self.eid = None
                    self.tag = None
                    self.module = None
                    self.gen_location = None
                    self.severity = None
                    self.group = None
                    self.description = None
                    self.set_time = None
                    self.clear_time = None
                    self._segment_path = lambda: "history" + "[aid='" + str(self.aid) + "']" + "[eid='" + str(self.eid) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-alarm-mgr:alarm_mgr/brief/system/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AlarmMgr.Brief.System.History, ['aid', 'eid', 'tag', 'module', 'gen_location', 'severity', 'group', 'description', 'set_time', 'clear_time'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_alarm_mgr as meta
                    return meta._meta_table['AlarmMgr.Brief.System.History']['meta_info']


            class Suppressed(_Entity_):
                """
                
                
                .. attribute:: aid  (key)
                
                	The AID for the current alarm
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: eid  (key)
                
                	The Object Id for the current alarm
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: tag
                
                	The Fault Tag for the current alarm
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: module
                
                	The Module for the current alarm
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: gen_location
                
                	The location for the current alarm
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: severity
                
                	The alarm severity
                	**type**\:  :py:class:`SeverityTd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.SeverityTd>`
                
                	**config**\: False
                
                .. attribute:: group
                
                	The alarm grouping 
                	**type**\:  :py:class:`GroupTd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.GroupTd>`
                
                	**config**\: False
                
                .. attribute:: description
                
                	Alarm description
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: set_time
                
                	Alarm set time stamp
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: suppressed_time
                
                	Alarm suppressed time stamp
                	**type**\: str
                
                	**config**\: False
                
                

                """

                _prefix = 'alarms'
                _revision = '2018-04-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(AlarmMgr.Brief.System.Suppressed, self).__init__()

                    self.yang_name = "suppressed"
                    self.yang_parent_name = "system"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['aid','eid']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('aid', (YLeaf(YType.str, 'aid'), ['str'])),
                        ('eid', (YLeaf(YType.str, 'eid'), ['str'])),
                        ('tag', (YLeaf(YType.str, 'tag'), ['str'])),
                        ('module', (YLeaf(YType.str, 'module'), ['str'])),
                        ('gen_location', (YLeaf(YType.str, 'gen_location'), ['str'])),
                        ('severity', (YLeaf(YType.enumeration, 'severity'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr', 'SeverityTd', '')])),
                        ('group', (YLeaf(YType.enumeration, 'group'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr', 'GroupTd', '')])),
                        ('description', (YLeaf(YType.str, 'description'), ['str'])),
                        ('set_time', (YLeaf(YType.str, 'set_time'), ['str'])),
                        ('suppressed_time', (YLeaf(YType.str, 'suppressed_time'), ['str'])),
                    ])
                    self.aid = None
                    self.eid = None
                    self.tag = None
                    self.module = None
                    self.gen_location = None
                    self.severity = None
                    self.group = None
                    self.description = None
                    self.set_time = None
                    self.suppressed_time = None
                    self._segment_path = lambda: "suppressed" + "[aid='" + str(self.aid) + "']" + "[eid='" + str(self.eid) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-alarm-mgr:alarm_mgr/brief/system/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AlarmMgr.Brief.System.Suppressed, ['aid', 'eid', 'tag', 'module', 'gen_location', 'severity', 'group', 'description', 'set_time', 'suppressed_time'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_alarm_mgr as meta
                    return meta._meta_table['AlarmMgr.Brief.System.Suppressed']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_alarm_mgr as meta
                return meta._meta_table['AlarmMgr.Brief.System']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_alarm_mgr as meta
            return meta._meta_table['AlarmMgr.Brief']['meta_info']


    class Detail(_Entity_):
        """
        A set of detail alarm commands
        
        .. attribute:: card
        
        	Alarms reported at the local card as specified by the location parameter
        	**type**\:  :py:class:`Card <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.AlarmMgr.Detail.Card>`
        
        	**config**\: False
        
        .. attribute:: rack
        
        	Alarms reported at the rack as specified by the location parameter
        	**type**\:  :py:class:`Rack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.AlarmMgr.Detail.Rack>`
        
        	**config**\: False
        
        .. attribute:: system
        
        	Alarms reported at the system as specified by the location parameter
        	**type**\:  :py:class:`System <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.AlarmMgr.Detail.System>`
        
        	**config**\: False
        
        

        """

        _prefix = 'alarms'
        _revision = '2018-04-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(AlarmMgr.Detail, self).__init__()

            self.yang_name = "detail"
            self.yang_parent_name = "alarm_mgr"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("card", ("card", AlarmMgr.Detail.Card)), ("rack", ("rack", AlarmMgr.Detail.Rack)), ("system", ("system", AlarmMgr.Detail.System))])
            self._leafs = OrderedDict()

            self.card = AlarmMgr.Detail.Card()
            self.card.parent = self
            self._children_name_map["card"] = "card"

            self.rack = AlarmMgr.Detail.Rack()
            self.rack.parent = self
            self._children_name_map["rack"] = "rack"

            self.system = AlarmMgr.Detail.System()
            self.system.parent = self
            self._children_name_map["system"] = "system"
            self._segment_path = lambda: "detail"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-alarm-mgr:alarm_mgr/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(AlarmMgr.Detail, [], name, value)


        class Card(_Entity_):
            """
            Alarms reported at the local card as
            specified by the location parameter
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.AlarmMgr.Detail.Card.Location>`
            
            	**config**\: False
            
            

            """

            _prefix = 'alarms'
            _revision = '2018-04-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(AlarmMgr.Detail.Card, self).__init__()

                self.yang_name = "card"
                self.yang_parent_name = "detail"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("location", ("location", AlarmMgr.Detail.Card.Location))])
                self._leafs = OrderedDict()

                self.location = YList(self)
                self._segment_path = lambda: "card"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-alarm-mgr:alarm_mgr/detail/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(AlarmMgr.Detail.Card, [], name, value)


            class Location(_Entity_):
                """
                
                
                .. attribute:: locations  (key)
                
                	
                	**type**\: str
                
                	**pattern:** ((([bB][0\-9])/(([a\-zA\-Z]){2}\\d{1,2}))\|(([fF][0\-7])/(([a\-zA\-Z]){2}\\d{1,2}))\|((0?[0\-9]\|1[0\-5])/((([a\-zA\-Z]){2,3})?\\d{1,2})))(/[cC][pP][uU]0)?
                
                	**config**\: False
                
                .. attribute:: active
                
                	
                	**type**\: list of  		 :py:class:`Active <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.AlarmMgr.Detail.Card.Location.Active>`
                
                	**config**\: False
                
                .. attribute:: history
                
                	
                	**type**\: list of  		 :py:class:`History <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.AlarmMgr.Detail.Card.Location.History>`
                
                	**config**\: False
                
                .. attribute:: stats
                
                	
                	**type**\: list of  		 :py:class:`Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.AlarmMgr.Detail.Card.Location.Stats>`
                
                	**config**\: False
                
                .. attribute:: clients
                
                	
                	**type**\: list of  		 :py:class:`Clients <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.AlarmMgr.Detail.Card.Location.Clients>`
                
                	**config**\: False
                
                .. attribute:: suppressed
                
                	
                	**type**\: list of  		 :py:class:`Suppressed <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.AlarmMgr.Detail.Card.Location.Suppressed>`
                
                	**config**\: False
                
                

                """

                _prefix = 'alarms'
                _revision = '2018-04-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(AlarmMgr.Detail.Card.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "card"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['locations']
                    self._child_classes = OrderedDict([("active", ("active", AlarmMgr.Detail.Card.Location.Active)), ("history", ("history", AlarmMgr.Detail.Card.Location.History)), ("stats", ("stats", AlarmMgr.Detail.Card.Location.Stats)), ("clients", ("clients", AlarmMgr.Detail.Card.Location.Clients)), ("suppressed", ("suppressed", AlarmMgr.Detail.Card.Location.Suppressed))])
                    self._leafs = OrderedDict([
                        ('locations', (YLeaf(YType.str, 'locations'), ['str'])),
                    ])
                    self.locations = None

                    self.active = YList(self)
                    self.history = YList(self)
                    self.stats = YList(self)
                    self.clients = YList(self)
                    self.suppressed = YList(self)
                    self._segment_path = lambda: "location" + "[locations='" + str(self.locations) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-alarm-mgr:alarm_mgr/detail/card/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AlarmMgr.Detail.Card.Location, ['locations'], name, value)


                class Active(_Entity_):
                    """
                    
                    
                    .. attribute:: aid  (key)
                    
                    	The AID for the current alarm
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: eid  (key)
                    
                    	The Object Id for the current alarm
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: tag
                    
                    	The Fault Tag for the current alarm
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: module
                    
                    	The Module for the current alarm
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: gen_location
                    
                    	The location for the current alarm
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: severity
                    
                    	The alarm severity
                    	**type**\:  :py:class:`SeverityTd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.SeverityTd>`
                    
                    	**config**\: False
                    
                    .. attribute:: group
                    
                    	The alarm grouping 
                    	**type**\:  :py:class:`GroupTd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.GroupTd>`
                    
                    	**config**\: False
                    
                    .. attribute:: description
                    
                    	Alarm description
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: set_time
                    
                    	Alarm set time stamp
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: state
                    
                    	The current state of the bi\-state alarm
                    	**type**\:  :py:class:`StatusTd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.StatusTd>`
                    
                    	**config**\: False
                    
                    .. attribute:: reporting_agent_id
                    
                    	The reporting agent id
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: resynced
                    
                    	The condition bit\-flags of the alarm
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: detail_desc
                    
                    	Alarm detailed description
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: clear_time
                    
                    	Alarm clear time stamp
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'alarms'
                    _revision = '2018-04-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(AlarmMgr.Detail.Card.Location.Active, self).__init__()

                        self.yang_name = "active"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['aid','eid']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('aid', (YLeaf(YType.str, 'aid'), ['str'])),
                            ('eid', (YLeaf(YType.str, 'eid'), ['str'])),
                            ('tag', (YLeaf(YType.str, 'tag'), ['str'])),
                            ('module', (YLeaf(YType.str, 'module'), ['str'])),
                            ('gen_location', (YLeaf(YType.str, 'gen_location'), ['str'])),
                            ('severity', (YLeaf(YType.enumeration, 'severity'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr', 'SeverityTd', '')])),
                            ('group', (YLeaf(YType.enumeration, 'group'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr', 'GroupTd', '')])),
                            ('description', (YLeaf(YType.str, 'description'), ['str'])),
                            ('set_time', (YLeaf(YType.str, 'set_time'), ['str'])),
                            ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr', 'StatusTd', '')])),
                            ('reporting_agent_id', (YLeaf(YType.uint32, 'reporting_agent_id'), ['int'])),
                            ('resynced', (YLeaf(YType.uint32, 'resynced'), ['int'])),
                            ('detail_desc', (YLeaf(YType.str, 'detail_desc'), ['str'])),
                            ('clear_time', (YLeaf(YType.str, 'clear_time'), ['str'])),
                        ])
                        self.aid = None
                        self.eid = None
                        self.tag = None
                        self.module = None
                        self.gen_location = None
                        self.severity = None
                        self.group = None
                        self.description = None
                        self.set_time = None
                        self.state = None
                        self.reporting_agent_id = None
                        self.resynced = None
                        self.detail_desc = None
                        self.clear_time = None
                        self._segment_path = lambda: "active" + "[aid='" + str(self.aid) + "']" + "[eid='" + str(self.eid) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AlarmMgr.Detail.Card.Location.Active, ['aid', 'eid', 'tag', 'module', 'gen_location', 'severity', 'group', 'description', 'set_time', 'state', 'reporting_agent_id', 'resynced', 'detail_desc', 'clear_time'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_alarm_mgr as meta
                        return meta._meta_table['AlarmMgr.Detail.Card.Location.Active']['meta_info']


                class History(_Entity_):
                    """
                    
                    
                    .. attribute:: aid  (key)
                    
                    	The AID for the current alarm
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: eid  (key)
                    
                    	The Object Id for the current alarm
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: tag
                    
                    	The Fault Tag for the current alarm
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: module
                    
                    	The Module for the current alarm
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: gen_location
                    
                    	The location for the current alarm
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: severity
                    
                    	The alarm severity
                    	**type**\:  :py:class:`SeverityTd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.SeverityTd>`
                    
                    	**config**\: False
                    
                    .. attribute:: group
                    
                    	The alarm grouping 
                    	**type**\:  :py:class:`GroupTd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.GroupTd>`
                    
                    	**config**\: False
                    
                    .. attribute:: description
                    
                    	Alarm description
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: set_time
                    
                    	Alarm set time stamp
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: state
                    
                    	The current state of the bi\-state alarm
                    	**type**\:  :py:class:`StatusTd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.StatusTd>`
                    
                    	**config**\: False
                    
                    .. attribute:: reporting_agent_id
                    
                    	The reporting agent id
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: resynced
                    
                    	The condition bit\-flags of the alarm
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: detail_desc
                    
                    	Alarm detailed description
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: clear_time
                    
                    	Alarm clear time stamp
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'alarms'
                    _revision = '2018-04-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(AlarmMgr.Detail.Card.Location.History, self).__init__()

                        self.yang_name = "history"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['aid','eid']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('aid', (YLeaf(YType.str, 'aid'), ['str'])),
                            ('eid', (YLeaf(YType.str, 'eid'), ['str'])),
                            ('tag', (YLeaf(YType.str, 'tag'), ['str'])),
                            ('module', (YLeaf(YType.str, 'module'), ['str'])),
                            ('gen_location', (YLeaf(YType.str, 'gen_location'), ['str'])),
                            ('severity', (YLeaf(YType.enumeration, 'severity'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr', 'SeverityTd', '')])),
                            ('group', (YLeaf(YType.enumeration, 'group'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr', 'GroupTd', '')])),
                            ('description', (YLeaf(YType.str, 'description'), ['str'])),
                            ('set_time', (YLeaf(YType.str, 'set_time'), ['str'])),
                            ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr', 'StatusTd', '')])),
                            ('reporting_agent_id', (YLeaf(YType.uint32, 'reporting_agent_id'), ['int'])),
                            ('resynced', (YLeaf(YType.uint32, 'resynced'), ['int'])),
                            ('detail_desc', (YLeaf(YType.str, 'detail_desc'), ['str'])),
                            ('clear_time', (YLeaf(YType.str, 'clear_time'), ['str'])),
                        ])
                        self.aid = None
                        self.eid = None
                        self.tag = None
                        self.module = None
                        self.gen_location = None
                        self.severity = None
                        self.group = None
                        self.description = None
                        self.set_time = None
                        self.state = None
                        self.reporting_agent_id = None
                        self.resynced = None
                        self.detail_desc = None
                        self.clear_time = None
                        self._segment_path = lambda: "history" + "[aid='" + str(self.aid) + "']" + "[eid='" + str(self.eid) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AlarmMgr.Detail.Card.Location.History, ['aid', 'eid', 'tag', 'module', 'gen_location', 'severity', 'group', 'description', 'set_time', 'state', 'reporting_agent_id', 'resynced', 'detail_desc', 'clear_time'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_alarm_mgr as meta
                        return meta._meta_table['AlarmMgr.Detail.Card.Location.History']['meta_info']


                class Stats(_Entity_):
                    """
                    
                    
                    .. attribute:: attime  (key)
                    
                    	Alarms statistics at specified time
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: reported
                    
                    	Total alarms reported into this service
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: dropped
                    
                    	Alarms dropped due to some error or other
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: bi_set
                    
                    	Total active alarms current in this service
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: bi_clear
                    
                    	Alarms that are currently in the cleared state
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: suppressed
                    
                    	Alarms that are currently in the suppressed state
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: drop_inv_aid
                    
                    	Alarms dropped due to invalid aid in the alarm report
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: drop_no_mem
                    
                    	Alarms dropped due to low memory condition
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: drop_db_error
                    
                    	Alarms dropped due to database internal error
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: drop_clear_no_set
                    
                    	Alarms dropped due to clear without a set
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: drop_dup
                    
                    	Alarms dropped due to duplicate alarm report
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: cache_hit
                    
                    	Alarms present in the cached for show
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: cache_miss
                    
                    	Alarms not present in the cached for show
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'alarms'
                    _revision = '2018-04-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(AlarmMgr.Detail.Card.Location.Stats, self).__init__()

                        self.yang_name = "stats"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['attime']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('attime', (YLeaf(YType.str, 'attime'), ['str'])),
                            ('reported', (YLeaf(YType.uint64, 'reported'), ['int'])),
                            ('dropped', (YLeaf(YType.uint64, 'dropped'), ['int'])),
                            ('bi_set', (YLeaf(YType.uint64, 'bi_set'), ['int'])),
                            ('bi_clear', (YLeaf(YType.uint64, 'bi_clear'), ['int'])),
                            ('suppressed', (YLeaf(YType.uint64, 'suppressed'), ['int'])),
                            ('drop_inv_aid', (YLeaf(YType.uint64, 'drop_inv_aid'), ['int'])),
                            ('drop_no_mem', (YLeaf(YType.uint64, 'drop_no_mem'), ['int'])),
                            ('drop_db_error', (YLeaf(YType.uint64, 'drop_db_error'), ['int'])),
                            ('drop_clear_no_set', (YLeaf(YType.uint64, 'drop_clear_no_set'), ['int'])),
                            ('drop_dup', (YLeaf(YType.uint64, 'drop_dup'), ['int'])),
                            ('cache_hit', (YLeaf(YType.uint64, 'cache_hit'), ['int'])),
                            ('cache_miss', (YLeaf(YType.uint64, 'cache_miss'), ['int'])),
                        ])
                        self.attime = None
                        self.reported = None
                        self.dropped = None
                        self.bi_set = None
                        self.bi_clear = None
                        self.suppressed = None
                        self.drop_inv_aid = None
                        self.drop_no_mem = None
                        self.drop_db_error = None
                        self.drop_clear_no_set = None
                        self.drop_dup = None
                        self.cache_hit = None
                        self.cache_miss = None
                        self._segment_path = lambda: "stats" + "[attime='" + str(self.attime) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AlarmMgr.Detail.Card.Location.Stats, ['attime', 'reported', 'dropped', 'bi_set', 'bi_clear', 'suppressed', 'drop_inv_aid', 'drop_no_mem', 'drop_db_error', 'drop_clear_no_set', 'drop_dup', 'cache_hit', 'cache_miss'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_alarm_mgr as meta
                        return meta._meta_table['AlarmMgr.Detail.Card.Location.Stats']['meta_info']


                class Clients(_Entity_):
                    """
                    
                    
                    .. attribute:: agent_handle  (key)
                    
                    	The client handle through which interface
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: agent_name
                    
                    	Alarms client
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: agent_id
                    
                    	Alarms agent id of the client
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: agent_location
                    
                    	The location of this client
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: agent_state
                    
                    	The current state of the client
                    	**type**\:  :py:class:`AgentStateTd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.AgentStateTd>`
                    
                    	**config**\: False
                    
                    .. attribute:: agent_type
                    
                    	The type of  the client
                    	**type**\:  :py:class:`AgentTypeTd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.AgentTypeTd>`
                    
                    	**config**\: False
                    
                    .. attribute:: agent_filter_disp
                    
                    	The current subscription status of the client
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: agent_subs_id
                    
                    	The subscriber id of the client
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: agent_filter_state
                    
                    	The filter used for alarm bi\-state state
                    	**type**\:  :py:class:`StatusTd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.StatusTd>`
                    
                    	**config**\: False
                    
                    .. attribute:: agent_filter_severity
                    
                    	The filter used for alarm severity
                    	**type**\:  :py:class:`SeverityTd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.SeverityTd>`
                    
                    	**config**\: False
                    
                    .. attribute:: agent_filter_group
                    
                    	The filter used for alarm group
                    	**type**\:  :py:class:`GroupTd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.GroupTd>`
                    
                    	**config**\: False
                    
                    .. attribute:: agent_sdr_id
                    
                    	agent alarm\_sm register with sdr\_id in SOMT mode
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: agent_connect_count
                    
                    	Number of times the agent connected to the alarm mgr
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: agent_connect_time
                    
                    	Agent connect timestamp
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: agent_get_count
                    
                    	Number of times the agent queried for alarms
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: agent_subscribe_count
                    
                    	Number of times the agent subscribed for alarms
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: agent_report_count
                    
                    	Number of times the agent reported alarms
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'alarms'
                    _revision = '2018-04-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(AlarmMgr.Detail.Card.Location.Clients, self).__init__()

                        self.yang_name = "clients"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['agent_handle']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('agent_handle', (YLeaf(YType.str, 'agent_handle'), ['str'])),
                            ('agent_name', (YLeaf(YType.str, 'agent_name'), ['str'])),
                            ('agent_id', (YLeaf(YType.uint32, 'agent_id'), ['int'])),
                            ('agent_location', (YLeaf(YType.str, 'agent_location'), ['str'])),
                            ('agent_state', (YLeaf(YType.enumeration, 'agent_state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr', 'AgentStateTd', '')])),
                            ('agent_type', (YLeaf(YType.enumeration, 'agent_type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr', 'AgentTypeTd', '')])),
                            ('agent_filter_disp', (YLeaf(YType.boolean, 'agent_filter_disp'), ['bool'])),
                            ('agent_subs_id', (YLeaf(YType.uint32, 'agent_subs_id'), ['int'])),
                            ('agent_filter_state', (YLeaf(YType.enumeration, 'agent_filter_state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr', 'StatusTd', '')])),
                            ('agent_filter_severity', (YLeaf(YType.enumeration, 'agent_filter_severity'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr', 'SeverityTd', '')])),
                            ('agent_filter_group', (YLeaf(YType.enumeration, 'agent_filter_group'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr', 'GroupTd', '')])),
                            ('agent_sdr_id', (YLeaf(YType.uint32, 'agent_sdr_id'), ['int'])),
                            ('agent_connect_count', (YLeaf(YType.uint64, 'agent_connect_count'), ['int'])),
                            ('agent_connect_time', (YLeaf(YType.str, 'agent_connect_time'), ['str'])),
                            ('agent_get_count', (YLeaf(YType.uint64, 'agent_get_count'), ['int'])),
                            ('agent_subscribe_count', (YLeaf(YType.uint64, 'agent_subscribe_count'), ['int'])),
                            ('agent_report_count', (YLeaf(YType.uint64, 'agent_report_count'), ['int'])),
                        ])
                        self.agent_handle = None
                        self.agent_name = None
                        self.agent_id = None
                        self.agent_location = None
                        self.agent_state = None
                        self.agent_type = None
                        self.agent_filter_disp = None
                        self.agent_subs_id = None
                        self.agent_filter_state = None
                        self.agent_filter_severity = None
                        self.agent_filter_group = None
                        self.agent_sdr_id = None
                        self.agent_connect_count = None
                        self.agent_connect_time = None
                        self.agent_get_count = None
                        self.agent_subscribe_count = None
                        self.agent_report_count = None
                        self._segment_path = lambda: "clients" + "[agent_handle='" + str(self.agent_handle) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AlarmMgr.Detail.Card.Location.Clients, ['agent_handle', 'agent_name', 'agent_id', 'agent_location', 'agent_state', 'agent_type', 'agent_filter_disp', 'agent_subs_id', 'agent_filter_state', 'agent_filter_severity', 'agent_filter_group', 'agent_sdr_id', 'agent_connect_count', 'agent_connect_time', 'agent_get_count', 'agent_subscribe_count', 'agent_report_count'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_alarm_mgr as meta
                        return meta._meta_table['AlarmMgr.Detail.Card.Location.Clients']['meta_info']


                class Suppressed(_Entity_):
                    """
                    
                    
                    .. attribute:: aid  (key)
                    
                    	The AID for the current alarm
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: eid  (key)
                    
                    	The Object Id for the current alarm
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: tag
                    
                    	The Fault Tag for the current alarm
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: module
                    
                    	The Module for the current alarm
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: gen_location
                    
                    	The location for the current alarm
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: severity
                    
                    	The alarm severity
                    	**type**\:  :py:class:`SeverityTd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.SeverityTd>`
                    
                    	**config**\: False
                    
                    .. attribute:: group
                    
                    	The alarm grouping 
                    	**type**\:  :py:class:`GroupTd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.GroupTd>`
                    
                    	**config**\: False
                    
                    .. attribute:: description
                    
                    	Alarm description
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: set_time
                    
                    	Alarm set time stamp
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: state
                    
                    	The current state of the bi\-state alarm
                    	**type**\:  :py:class:`StatusTd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.StatusTd>`
                    
                    	**config**\: False
                    
                    .. attribute:: reporting_agent_id
                    
                    	The reporting agent id
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: resynced
                    
                    	The condition bit\-flags of the alarm
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: detail_desc
                    
                    	Alarm detailed description
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: suppressed_time
                    
                    	Alarm suppressed time stamp
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'alarms'
                    _revision = '2018-04-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(AlarmMgr.Detail.Card.Location.Suppressed, self).__init__()

                        self.yang_name = "suppressed"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['aid','eid']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('aid', (YLeaf(YType.str, 'aid'), ['str'])),
                            ('eid', (YLeaf(YType.str, 'eid'), ['str'])),
                            ('tag', (YLeaf(YType.str, 'tag'), ['str'])),
                            ('module', (YLeaf(YType.str, 'module'), ['str'])),
                            ('gen_location', (YLeaf(YType.str, 'gen_location'), ['str'])),
                            ('severity', (YLeaf(YType.enumeration, 'severity'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr', 'SeverityTd', '')])),
                            ('group', (YLeaf(YType.enumeration, 'group'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr', 'GroupTd', '')])),
                            ('description', (YLeaf(YType.str, 'description'), ['str'])),
                            ('set_time', (YLeaf(YType.str, 'set_time'), ['str'])),
                            ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr', 'StatusTd', '')])),
                            ('reporting_agent_id', (YLeaf(YType.uint32, 'reporting_agent_id'), ['int'])),
                            ('resynced', (YLeaf(YType.uint32, 'resynced'), ['int'])),
                            ('detail_desc', (YLeaf(YType.str, 'detail_desc'), ['str'])),
                            ('suppressed_time', (YLeaf(YType.str, 'suppressed_time'), ['str'])),
                        ])
                        self.aid = None
                        self.eid = None
                        self.tag = None
                        self.module = None
                        self.gen_location = None
                        self.severity = None
                        self.group = None
                        self.description = None
                        self.set_time = None
                        self.state = None
                        self.reporting_agent_id = None
                        self.resynced = None
                        self.detail_desc = None
                        self.suppressed_time = None
                        self._segment_path = lambda: "suppressed" + "[aid='" + str(self.aid) + "']" + "[eid='" + str(self.eid) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AlarmMgr.Detail.Card.Location.Suppressed, ['aid', 'eid', 'tag', 'module', 'gen_location', 'severity', 'group', 'description', 'set_time', 'state', 'reporting_agent_id', 'resynced', 'detail_desc', 'suppressed_time'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_alarm_mgr as meta
                        return meta._meta_table['AlarmMgr.Detail.Card.Location.Suppressed']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_alarm_mgr as meta
                    return meta._meta_table['AlarmMgr.Detail.Card.Location']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_alarm_mgr as meta
                return meta._meta_table['AlarmMgr.Detail.Card']['meta_info']


        class Rack(_Entity_):
            """
            Alarms reported at the rack as
            specified by the location parameter
            
            .. attribute:: rack_locations
            
            	
            	**type**\: list of  		 :py:class:`RackLocations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.AlarmMgr.Detail.Rack.RackLocations>`
            
            	**config**\: False
            
            

            """

            _prefix = 'alarms'
            _revision = '2018-04-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(AlarmMgr.Detail.Rack, self).__init__()

                self.yang_name = "rack"
                self.yang_parent_name = "detail"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("rack_locations", ("rack_locations", AlarmMgr.Detail.Rack.RackLocations))])
                self._leafs = OrderedDict()

                self.rack_locations = YList(self)
                self._segment_path = lambda: "rack"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-alarm-mgr:alarm_mgr/detail/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(AlarmMgr.Detail.Rack, [], name, value)


            class RackLocations(_Entity_):
                """
                
                
                .. attribute:: rackid  (key)
                
                	
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: active
                
                	
                	**type**\: list of  		 :py:class:`Active <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.AlarmMgr.Detail.Rack.RackLocations.Active>`
                
                	**config**\: False
                
                .. attribute:: history
                
                	
                	**type**\: list of  		 :py:class:`History <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.AlarmMgr.Detail.Rack.RackLocations.History>`
                
                	**config**\: False
                
                .. attribute:: stats
                
                	
                	**type**\: list of  		 :py:class:`Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.AlarmMgr.Detail.Rack.RackLocations.Stats>`
                
                	**config**\: False
                
                .. attribute:: clients
                
                	
                	**type**\: list of  		 :py:class:`Clients <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.AlarmMgr.Detail.Rack.RackLocations.Clients>`
                
                	**config**\: False
                
                .. attribute:: suppressed
                
                	
                	**type**\: list of  		 :py:class:`Suppressed <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.AlarmMgr.Detail.Rack.RackLocations.Suppressed>`
                
                	**config**\: False
                
                

                """

                _prefix = 'alarms'
                _revision = '2018-04-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(AlarmMgr.Detail.Rack.RackLocations, self).__init__()

                    self.yang_name = "rack_locations"
                    self.yang_parent_name = "rack"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['rackid']
                    self._child_classes = OrderedDict([("active", ("active", AlarmMgr.Detail.Rack.RackLocations.Active)), ("history", ("history", AlarmMgr.Detail.Rack.RackLocations.History)), ("stats", ("stats", AlarmMgr.Detail.Rack.RackLocations.Stats)), ("clients", ("clients", AlarmMgr.Detail.Rack.RackLocations.Clients)), ("suppressed", ("suppressed", AlarmMgr.Detail.Rack.RackLocations.Suppressed))])
                    self._leafs = OrderedDict([
                        ('rackid', (YLeaf(YType.uint32, 'rackid'), ['int'])),
                    ])
                    self.rackid = None

                    self.active = YList(self)
                    self.history = YList(self)
                    self.stats = YList(self)
                    self.clients = YList(self)
                    self.suppressed = YList(self)
                    self._segment_path = lambda: "rack_locations" + "[rackid='" + str(self.rackid) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-alarm-mgr:alarm_mgr/detail/rack/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AlarmMgr.Detail.Rack.RackLocations, ['rackid'], name, value)


                class Active(_Entity_):
                    """
                    
                    
                    .. attribute:: aid  (key)
                    
                    	The AID for the current alarm
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: eid  (key)
                    
                    	The Object Id for the current alarm
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: tag
                    
                    	The Fault Tag for the current alarm
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: module
                    
                    	The Module for the current alarm
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: gen_location
                    
                    	The location for the current alarm
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: severity
                    
                    	The alarm severity
                    	**type**\:  :py:class:`SeverityTd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.SeverityTd>`
                    
                    	**config**\: False
                    
                    .. attribute:: group
                    
                    	The alarm grouping 
                    	**type**\:  :py:class:`GroupTd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.GroupTd>`
                    
                    	**config**\: False
                    
                    .. attribute:: description
                    
                    	Alarm description
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: set_time
                    
                    	Alarm set time stamp
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: state
                    
                    	The current state of the bi\-state alarm
                    	**type**\:  :py:class:`StatusTd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.StatusTd>`
                    
                    	**config**\: False
                    
                    .. attribute:: reporting_agent_id
                    
                    	The reporting agent id
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: resynced
                    
                    	The condition bit\-flags of the alarm
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: detail_desc
                    
                    	Alarm detailed description
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: clear_time
                    
                    	Alarm clear time stamp
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'alarms'
                    _revision = '2018-04-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(AlarmMgr.Detail.Rack.RackLocations.Active, self).__init__()

                        self.yang_name = "active"
                        self.yang_parent_name = "rack_locations"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['aid','eid']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('aid', (YLeaf(YType.str, 'aid'), ['str'])),
                            ('eid', (YLeaf(YType.str, 'eid'), ['str'])),
                            ('tag', (YLeaf(YType.str, 'tag'), ['str'])),
                            ('module', (YLeaf(YType.str, 'module'), ['str'])),
                            ('gen_location', (YLeaf(YType.str, 'gen_location'), ['str'])),
                            ('severity', (YLeaf(YType.enumeration, 'severity'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr', 'SeverityTd', '')])),
                            ('group', (YLeaf(YType.enumeration, 'group'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr', 'GroupTd', '')])),
                            ('description', (YLeaf(YType.str, 'description'), ['str'])),
                            ('set_time', (YLeaf(YType.str, 'set_time'), ['str'])),
                            ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr', 'StatusTd', '')])),
                            ('reporting_agent_id', (YLeaf(YType.uint32, 'reporting_agent_id'), ['int'])),
                            ('resynced', (YLeaf(YType.uint32, 'resynced'), ['int'])),
                            ('detail_desc', (YLeaf(YType.str, 'detail_desc'), ['str'])),
                            ('clear_time', (YLeaf(YType.str, 'clear_time'), ['str'])),
                        ])
                        self.aid = None
                        self.eid = None
                        self.tag = None
                        self.module = None
                        self.gen_location = None
                        self.severity = None
                        self.group = None
                        self.description = None
                        self.set_time = None
                        self.state = None
                        self.reporting_agent_id = None
                        self.resynced = None
                        self.detail_desc = None
                        self.clear_time = None
                        self._segment_path = lambda: "active" + "[aid='" + str(self.aid) + "']" + "[eid='" + str(self.eid) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AlarmMgr.Detail.Rack.RackLocations.Active, ['aid', 'eid', 'tag', 'module', 'gen_location', 'severity', 'group', 'description', 'set_time', 'state', 'reporting_agent_id', 'resynced', 'detail_desc', 'clear_time'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_alarm_mgr as meta
                        return meta._meta_table['AlarmMgr.Detail.Rack.RackLocations.Active']['meta_info']


                class History(_Entity_):
                    """
                    
                    
                    .. attribute:: aid  (key)
                    
                    	The AID for the current alarm
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: eid  (key)
                    
                    	The Object Id for the current alarm
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: tag
                    
                    	The Fault Tag for the current alarm
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: module
                    
                    	The Module for the current alarm
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: gen_location
                    
                    	The location for the current alarm
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: severity
                    
                    	The alarm severity
                    	**type**\:  :py:class:`SeverityTd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.SeverityTd>`
                    
                    	**config**\: False
                    
                    .. attribute:: group
                    
                    	The alarm grouping 
                    	**type**\:  :py:class:`GroupTd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.GroupTd>`
                    
                    	**config**\: False
                    
                    .. attribute:: description
                    
                    	Alarm description
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: set_time
                    
                    	Alarm set time stamp
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: state
                    
                    	The current state of the bi\-state alarm
                    	**type**\:  :py:class:`StatusTd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.StatusTd>`
                    
                    	**config**\: False
                    
                    .. attribute:: reporting_agent_id
                    
                    	The reporting agent id
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: resynced
                    
                    	The condition bit\-flags of the alarm
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: detail_desc
                    
                    	Alarm detailed description
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: clear_time
                    
                    	Alarm clear time stamp
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'alarms'
                    _revision = '2018-04-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(AlarmMgr.Detail.Rack.RackLocations.History, self).__init__()

                        self.yang_name = "history"
                        self.yang_parent_name = "rack_locations"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['aid','eid']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('aid', (YLeaf(YType.str, 'aid'), ['str'])),
                            ('eid', (YLeaf(YType.str, 'eid'), ['str'])),
                            ('tag', (YLeaf(YType.str, 'tag'), ['str'])),
                            ('module', (YLeaf(YType.str, 'module'), ['str'])),
                            ('gen_location', (YLeaf(YType.str, 'gen_location'), ['str'])),
                            ('severity', (YLeaf(YType.enumeration, 'severity'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr', 'SeverityTd', '')])),
                            ('group', (YLeaf(YType.enumeration, 'group'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr', 'GroupTd', '')])),
                            ('description', (YLeaf(YType.str, 'description'), ['str'])),
                            ('set_time', (YLeaf(YType.str, 'set_time'), ['str'])),
                            ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr', 'StatusTd', '')])),
                            ('reporting_agent_id', (YLeaf(YType.uint32, 'reporting_agent_id'), ['int'])),
                            ('resynced', (YLeaf(YType.uint32, 'resynced'), ['int'])),
                            ('detail_desc', (YLeaf(YType.str, 'detail_desc'), ['str'])),
                            ('clear_time', (YLeaf(YType.str, 'clear_time'), ['str'])),
                        ])
                        self.aid = None
                        self.eid = None
                        self.tag = None
                        self.module = None
                        self.gen_location = None
                        self.severity = None
                        self.group = None
                        self.description = None
                        self.set_time = None
                        self.state = None
                        self.reporting_agent_id = None
                        self.resynced = None
                        self.detail_desc = None
                        self.clear_time = None
                        self._segment_path = lambda: "history" + "[aid='" + str(self.aid) + "']" + "[eid='" + str(self.eid) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AlarmMgr.Detail.Rack.RackLocations.History, ['aid', 'eid', 'tag', 'module', 'gen_location', 'severity', 'group', 'description', 'set_time', 'state', 'reporting_agent_id', 'resynced', 'detail_desc', 'clear_time'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_alarm_mgr as meta
                        return meta._meta_table['AlarmMgr.Detail.Rack.RackLocations.History']['meta_info']


                class Stats(_Entity_):
                    """
                    
                    
                    .. attribute:: attime  (key)
                    
                    	Alarms statistics at specified time
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: reported
                    
                    	Total alarms reported into this service
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: dropped
                    
                    	Alarms dropped due to some error or other
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: bi_set
                    
                    	Total active alarms current in this service
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: bi_clear
                    
                    	Alarms that are currently in the cleared state
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: suppressed
                    
                    	Alarms that are currently in the suppressed state
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: drop_inv_aid
                    
                    	Alarms dropped due to invalid aid in the alarm report
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: drop_no_mem
                    
                    	Alarms dropped due to low memory condition
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: drop_db_error
                    
                    	Alarms dropped due to database internal error
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: drop_clear_no_set
                    
                    	Alarms dropped due to clear without a set
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: drop_dup
                    
                    	Alarms dropped due to duplicate alarm report
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: cache_hit
                    
                    	Alarms present in the cached for show
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: cache_miss
                    
                    	Alarms not present in the cached for show
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'alarms'
                    _revision = '2018-04-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(AlarmMgr.Detail.Rack.RackLocations.Stats, self).__init__()

                        self.yang_name = "stats"
                        self.yang_parent_name = "rack_locations"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['attime']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('attime', (YLeaf(YType.str, 'attime'), ['str'])),
                            ('reported', (YLeaf(YType.uint64, 'reported'), ['int'])),
                            ('dropped', (YLeaf(YType.uint64, 'dropped'), ['int'])),
                            ('bi_set', (YLeaf(YType.uint64, 'bi_set'), ['int'])),
                            ('bi_clear', (YLeaf(YType.uint64, 'bi_clear'), ['int'])),
                            ('suppressed', (YLeaf(YType.uint64, 'suppressed'), ['int'])),
                            ('drop_inv_aid', (YLeaf(YType.uint64, 'drop_inv_aid'), ['int'])),
                            ('drop_no_mem', (YLeaf(YType.uint64, 'drop_no_mem'), ['int'])),
                            ('drop_db_error', (YLeaf(YType.uint64, 'drop_db_error'), ['int'])),
                            ('drop_clear_no_set', (YLeaf(YType.uint64, 'drop_clear_no_set'), ['int'])),
                            ('drop_dup', (YLeaf(YType.uint64, 'drop_dup'), ['int'])),
                            ('cache_hit', (YLeaf(YType.uint64, 'cache_hit'), ['int'])),
                            ('cache_miss', (YLeaf(YType.uint64, 'cache_miss'), ['int'])),
                        ])
                        self.attime = None
                        self.reported = None
                        self.dropped = None
                        self.bi_set = None
                        self.bi_clear = None
                        self.suppressed = None
                        self.drop_inv_aid = None
                        self.drop_no_mem = None
                        self.drop_db_error = None
                        self.drop_clear_no_set = None
                        self.drop_dup = None
                        self.cache_hit = None
                        self.cache_miss = None
                        self._segment_path = lambda: "stats" + "[attime='" + str(self.attime) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AlarmMgr.Detail.Rack.RackLocations.Stats, ['attime', 'reported', 'dropped', 'bi_set', 'bi_clear', 'suppressed', 'drop_inv_aid', 'drop_no_mem', 'drop_db_error', 'drop_clear_no_set', 'drop_dup', 'cache_hit', 'cache_miss'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_alarm_mgr as meta
                        return meta._meta_table['AlarmMgr.Detail.Rack.RackLocations.Stats']['meta_info']


                class Clients(_Entity_):
                    """
                    
                    
                    .. attribute:: agent_handle  (key)
                    
                    	The client handle through which interface
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: agent_name
                    
                    	Alarms client
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: agent_id
                    
                    	Alarms agent id of the client
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: agent_location
                    
                    	The location of this client
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: agent_state
                    
                    	The current state of the client
                    	**type**\:  :py:class:`AgentStateTd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.AgentStateTd>`
                    
                    	**config**\: False
                    
                    .. attribute:: agent_type
                    
                    	The type of  the client
                    	**type**\:  :py:class:`AgentTypeTd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.AgentTypeTd>`
                    
                    	**config**\: False
                    
                    .. attribute:: agent_filter_disp
                    
                    	The current subscription status of the client
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: agent_subs_id
                    
                    	The subscriber id of the client
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: agent_filter_state
                    
                    	The filter used for alarm bi\-state state
                    	**type**\:  :py:class:`StatusTd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.StatusTd>`
                    
                    	**config**\: False
                    
                    .. attribute:: agent_filter_severity
                    
                    	The filter used for alarm severity
                    	**type**\:  :py:class:`SeverityTd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.SeverityTd>`
                    
                    	**config**\: False
                    
                    .. attribute:: agent_filter_group
                    
                    	The filter used for alarm group
                    	**type**\:  :py:class:`GroupTd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.GroupTd>`
                    
                    	**config**\: False
                    
                    .. attribute:: agent_sdr_id
                    
                    	agent alarm\_sm register with sdr\_id in SOMT mode
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: agent_connect_count
                    
                    	Number of times the agent connected to the alarm mgr
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: agent_connect_time
                    
                    	Agent connect timestamp
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: agent_get_count
                    
                    	Number of times the agent queried for alarms
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: agent_subscribe_count
                    
                    	Number of times the agent subscribed for alarms
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    .. attribute:: agent_report_count
                    
                    	Number of times the agent reported alarms
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'alarms'
                    _revision = '2018-04-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(AlarmMgr.Detail.Rack.RackLocations.Clients, self).__init__()

                        self.yang_name = "clients"
                        self.yang_parent_name = "rack_locations"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['agent_handle']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('agent_handle', (YLeaf(YType.str, 'agent_handle'), ['str'])),
                            ('agent_name', (YLeaf(YType.str, 'agent_name'), ['str'])),
                            ('agent_id', (YLeaf(YType.uint32, 'agent_id'), ['int'])),
                            ('agent_location', (YLeaf(YType.str, 'agent_location'), ['str'])),
                            ('agent_state', (YLeaf(YType.enumeration, 'agent_state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr', 'AgentStateTd', '')])),
                            ('agent_type', (YLeaf(YType.enumeration, 'agent_type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr', 'AgentTypeTd', '')])),
                            ('agent_filter_disp', (YLeaf(YType.boolean, 'agent_filter_disp'), ['bool'])),
                            ('agent_subs_id', (YLeaf(YType.uint32, 'agent_subs_id'), ['int'])),
                            ('agent_filter_state', (YLeaf(YType.enumeration, 'agent_filter_state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr', 'StatusTd', '')])),
                            ('agent_filter_severity', (YLeaf(YType.enumeration, 'agent_filter_severity'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr', 'SeverityTd', '')])),
                            ('agent_filter_group', (YLeaf(YType.enumeration, 'agent_filter_group'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr', 'GroupTd', '')])),
                            ('agent_sdr_id', (YLeaf(YType.uint32, 'agent_sdr_id'), ['int'])),
                            ('agent_connect_count', (YLeaf(YType.uint64, 'agent_connect_count'), ['int'])),
                            ('agent_connect_time', (YLeaf(YType.str, 'agent_connect_time'), ['str'])),
                            ('agent_get_count', (YLeaf(YType.uint64, 'agent_get_count'), ['int'])),
                            ('agent_subscribe_count', (YLeaf(YType.uint64, 'agent_subscribe_count'), ['int'])),
                            ('agent_report_count', (YLeaf(YType.uint64, 'agent_report_count'), ['int'])),
                        ])
                        self.agent_handle = None
                        self.agent_name = None
                        self.agent_id = None
                        self.agent_location = None
                        self.agent_state = None
                        self.agent_type = None
                        self.agent_filter_disp = None
                        self.agent_subs_id = None
                        self.agent_filter_state = None
                        self.agent_filter_severity = None
                        self.agent_filter_group = None
                        self.agent_sdr_id = None
                        self.agent_connect_count = None
                        self.agent_connect_time = None
                        self.agent_get_count = None
                        self.agent_subscribe_count = None
                        self.agent_report_count = None
                        self._segment_path = lambda: "clients" + "[agent_handle='" + str(self.agent_handle) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AlarmMgr.Detail.Rack.RackLocations.Clients, ['agent_handle', 'agent_name', 'agent_id', 'agent_location', 'agent_state', 'agent_type', 'agent_filter_disp', 'agent_subs_id', 'agent_filter_state', 'agent_filter_severity', 'agent_filter_group', 'agent_sdr_id', 'agent_connect_count', 'agent_connect_time', 'agent_get_count', 'agent_subscribe_count', 'agent_report_count'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_alarm_mgr as meta
                        return meta._meta_table['AlarmMgr.Detail.Rack.RackLocations.Clients']['meta_info']


                class Suppressed(_Entity_):
                    """
                    
                    
                    .. attribute:: aid  (key)
                    
                    	The AID for the current alarm
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: eid  (key)
                    
                    	The Object Id for the current alarm
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: tag
                    
                    	The Fault Tag for the current alarm
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: module
                    
                    	The Module for the current alarm
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: gen_location
                    
                    	The location for the current alarm
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: severity
                    
                    	The alarm severity
                    	**type**\:  :py:class:`SeverityTd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.SeverityTd>`
                    
                    	**config**\: False
                    
                    .. attribute:: group
                    
                    	The alarm grouping 
                    	**type**\:  :py:class:`GroupTd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.GroupTd>`
                    
                    	**config**\: False
                    
                    .. attribute:: description
                    
                    	Alarm description
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: set_time
                    
                    	Alarm set time stamp
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: state
                    
                    	The current state of the bi\-state alarm
                    	**type**\:  :py:class:`StatusTd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.StatusTd>`
                    
                    	**config**\: False
                    
                    .. attribute:: reporting_agent_id
                    
                    	The reporting agent id
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: resynced
                    
                    	The condition bit\-flags of the alarm
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: detail_desc
                    
                    	Alarm detailed description
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: suppressed_time
                    
                    	Alarm suppressed time stamp
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'alarms'
                    _revision = '2018-04-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(AlarmMgr.Detail.Rack.RackLocations.Suppressed, self).__init__()

                        self.yang_name = "suppressed"
                        self.yang_parent_name = "rack_locations"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['aid','eid']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('aid', (YLeaf(YType.str, 'aid'), ['str'])),
                            ('eid', (YLeaf(YType.str, 'eid'), ['str'])),
                            ('tag', (YLeaf(YType.str, 'tag'), ['str'])),
                            ('module', (YLeaf(YType.str, 'module'), ['str'])),
                            ('gen_location', (YLeaf(YType.str, 'gen_location'), ['str'])),
                            ('severity', (YLeaf(YType.enumeration, 'severity'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr', 'SeverityTd', '')])),
                            ('group', (YLeaf(YType.enumeration, 'group'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr', 'GroupTd', '')])),
                            ('description', (YLeaf(YType.str, 'description'), ['str'])),
                            ('set_time', (YLeaf(YType.str, 'set_time'), ['str'])),
                            ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr', 'StatusTd', '')])),
                            ('reporting_agent_id', (YLeaf(YType.uint32, 'reporting_agent_id'), ['int'])),
                            ('resynced', (YLeaf(YType.uint32, 'resynced'), ['int'])),
                            ('detail_desc', (YLeaf(YType.str, 'detail_desc'), ['str'])),
                            ('suppressed_time', (YLeaf(YType.str, 'suppressed_time'), ['str'])),
                        ])
                        self.aid = None
                        self.eid = None
                        self.tag = None
                        self.module = None
                        self.gen_location = None
                        self.severity = None
                        self.group = None
                        self.description = None
                        self.set_time = None
                        self.state = None
                        self.reporting_agent_id = None
                        self.resynced = None
                        self.detail_desc = None
                        self.suppressed_time = None
                        self._segment_path = lambda: "suppressed" + "[aid='" + str(self.aid) + "']" + "[eid='" + str(self.eid) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AlarmMgr.Detail.Rack.RackLocations.Suppressed, ['aid', 'eid', 'tag', 'module', 'gen_location', 'severity', 'group', 'description', 'set_time', 'state', 'reporting_agent_id', 'resynced', 'detail_desc', 'suppressed_time'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_alarm_mgr as meta
                        return meta._meta_table['AlarmMgr.Detail.Rack.RackLocations.Suppressed']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_alarm_mgr as meta
                    return meta._meta_table['AlarmMgr.Detail.Rack.RackLocations']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_alarm_mgr as meta
                return meta._meta_table['AlarmMgr.Detail.Rack']['meta_info']


        class System(_Entity_):
            """
            Alarms reported at the system as
            specified by the location parameter
            
            .. attribute:: active
            
            	
            	**type**\: list of  		 :py:class:`Active <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.AlarmMgr.Detail.System.Active>`
            
            	**config**\: False
            
            .. attribute:: history
            
            	
            	**type**\: list of  		 :py:class:`History <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.AlarmMgr.Detail.System.History>`
            
            	**config**\: False
            
            .. attribute:: stats
            
            	
            	**type**\: list of  		 :py:class:`Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.AlarmMgr.Detail.System.Stats>`
            
            	**config**\: False
            
            .. attribute:: clients
            
            	
            	**type**\: list of  		 :py:class:`Clients <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.AlarmMgr.Detail.System.Clients>`
            
            	**config**\: False
            
            .. attribute:: suppressed
            
            	
            	**type**\: list of  		 :py:class:`Suppressed <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.AlarmMgr.Detail.System.Suppressed>`
            
            	**config**\: False
            
            

            """

            _prefix = 'alarms'
            _revision = '2018-04-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(AlarmMgr.Detail.System, self).__init__()

                self.yang_name = "system"
                self.yang_parent_name = "detail"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("active", ("active", AlarmMgr.Detail.System.Active)), ("history", ("history", AlarmMgr.Detail.System.History)), ("stats", ("stats", AlarmMgr.Detail.System.Stats)), ("clients", ("clients", AlarmMgr.Detail.System.Clients)), ("suppressed", ("suppressed", AlarmMgr.Detail.System.Suppressed))])
                self._leafs = OrderedDict()

                self.active = YList(self)
                self.history = YList(self)
                self.stats = YList(self)
                self.clients = YList(self)
                self.suppressed = YList(self)
                self._segment_path = lambda: "system"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-alarm-mgr:alarm_mgr/detail/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(AlarmMgr.Detail.System, [], name, value)


            class Active(_Entity_):
                """
                
                
                .. attribute:: aid  (key)
                
                	The AID for the current alarm
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: eid  (key)
                
                	The Object Id for the current alarm
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: tag
                
                	The Fault Tag for the current alarm
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: module
                
                	The Module for the current alarm
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: gen_location
                
                	The location for the current alarm
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: severity
                
                	The alarm severity
                	**type**\:  :py:class:`SeverityTd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.SeverityTd>`
                
                	**config**\: False
                
                .. attribute:: group
                
                	The alarm grouping 
                	**type**\:  :py:class:`GroupTd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.GroupTd>`
                
                	**config**\: False
                
                .. attribute:: description
                
                	Alarm description
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: set_time
                
                	Alarm set time stamp
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: state
                
                	The current state of the bi\-state alarm
                	**type**\:  :py:class:`StatusTd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.StatusTd>`
                
                	**config**\: False
                
                .. attribute:: reporting_agent_id
                
                	The reporting agent id
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: resynced
                
                	The condition bit\-flags of the alarm
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: detail_desc
                
                	Alarm detailed description
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: clear_time
                
                	Alarm clear time stamp
                	**type**\: str
                
                	**config**\: False
                
                

                """

                _prefix = 'alarms'
                _revision = '2018-04-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(AlarmMgr.Detail.System.Active, self).__init__()

                    self.yang_name = "active"
                    self.yang_parent_name = "system"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['aid','eid']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('aid', (YLeaf(YType.str, 'aid'), ['str'])),
                        ('eid', (YLeaf(YType.str, 'eid'), ['str'])),
                        ('tag', (YLeaf(YType.str, 'tag'), ['str'])),
                        ('module', (YLeaf(YType.str, 'module'), ['str'])),
                        ('gen_location', (YLeaf(YType.str, 'gen_location'), ['str'])),
                        ('severity', (YLeaf(YType.enumeration, 'severity'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr', 'SeverityTd', '')])),
                        ('group', (YLeaf(YType.enumeration, 'group'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr', 'GroupTd', '')])),
                        ('description', (YLeaf(YType.str, 'description'), ['str'])),
                        ('set_time', (YLeaf(YType.str, 'set_time'), ['str'])),
                        ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr', 'StatusTd', '')])),
                        ('reporting_agent_id', (YLeaf(YType.uint32, 'reporting_agent_id'), ['int'])),
                        ('resynced', (YLeaf(YType.uint32, 'resynced'), ['int'])),
                        ('detail_desc', (YLeaf(YType.str, 'detail_desc'), ['str'])),
                        ('clear_time', (YLeaf(YType.str, 'clear_time'), ['str'])),
                    ])
                    self.aid = None
                    self.eid = None
                    self.tag = None
                    self.module = None
                    self.gen_location = None
                    self.severity = None
                    self.group = None
                    self.description = None
                    self.set_time = None
                    self.state = None
                    self.reporting_agent_id = None
                    self.resynced = None
                    self.detail_desc = None
                    self.clear_time = None
                    self._segment_path = lambda: "active" + "[aid='" + str(self.aid) + "']" + "[eid='" + str(self.eid) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-alarm-mgr:alarm_mgr/detail/system/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AlarmMgr.Detail.System.Active, ['aid', 'eid', 'tag', 'module', 'gen_location', 'severity', 'group', 'description', 'set_time', 'state', 'reporting_agent_id', 'resynced', 'detail_desc', 'clear_time'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_alarm_mgr as meta
                    return meta._meta_table['AlarmMgr.Detail.System.Active']['meta_info']


            class History(_Entity_):
                """
                
                
                .. attribute:: aid  (key)
                
                	The AID for the current alarm
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: eid  (key)
                
                	The Object Id for the current alarm
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: tag
                
                	The Fault Tag for the current alarm
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: module
                
                	The Module for the current alarm
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: gen_location
                
                	The location for the current alarm
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: severity
                
                	The alarm severity
                	**type**\:  :py:class:`SeverityTd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.SeverityTd>`
                
                	**config**\: False
                
                .. attribute:: group
                
                	The alarm grouping 
                	**type**\:  :py:class:`GroupTd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.GroupTd>`
                
                	**config**\: False
                
                .. attribute:: description
                
                	Alarm description
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: set_time
                
                	Alarm set time stamp
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: state
                
                	The current state of the bi\-state alarm
                	**type**\:  :py:class:`StatusTd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.StatusTd>`
                
                	**config**\: False
                
                .. attribute:: reporting_agent_id
                
                	The reporting agent id
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: resynced
                
                	The condition bit\-flags of the alarm
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: detail_desc
                
                	Alarm detailed description
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: clear_time
                
                	Alarm clear time stamp
                	**type**\: str
                
                	**config**\: False
                
                

                """

                _prefix = 'alarms'
                _revision = '2018-04-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(AlarmMgr.Detail.System.History, self).__init__()

                    self.yang_name = "history"
                    self.yang_parent_name = "system"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['aid','eid']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('aid', (YLeaf(YType.str, 'aid'), ['str'])),
                        ('eid', (YLeaf(YType.str, 'eid'), ['str'])),
                        ('tag', (YLeaf(YType.str, 'tag'), ['str'])),
                        ('module', (YLeaf(YType.str, 'module'), ['str'])),
                        ('gen_location', (YLeaf(YType.str, 'gen_location'), ['str'])),
                        ('severity', (YLeaf(YType.enumeration, 'severity'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr', 'SeverityTd', '')])),
                        ('group', (YLeaf(YType.enumeration, 'group'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr', 'GroupTd', '')])),
                        ('description', (YLeaf(YType.str, 'description'), ['str'])),
                        ('set_time', (YLeaf(YType.str, 'set_time'), ['str'])),
                        ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr', 'StatusTd', '')])),
                        ('reporting_agent_id', (YLeaf(YType.uint32, 'reporting_agent_id'), ['int'])),
                        ('resynced', (YLeaf(YType.uint32, 'resynced'), ['int'])),
                        ('detail_desc', (YLeaf(YType.str, 'detail_desc'), ['str'])),
                        ('clear_time', (YLeaf(YType.str, 'clear_time'), ['str'])),
                    ])
                    self.aid = None
                    self.eid = None
                    self.tag = None
                    self.module = None
                    self.gen_location = None
                    self.severity = None
                    self.group = None
                    self.description = None
                    self.set_time = None
                    self.state = None
                    self.reporting_agent_id = None
                    self.resynced = None
                    self.detail_desc = None
                    self.clear_time = None
                    self._segment_path = lambda: "history" + "[aid='" + str(self.aid) + "']" + "[eid='" + str(self.eid) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-alarm-mgr:alarm_mgr/detail/system/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AlarmMgr.Detail.System.History, ['aid', 'eid', 'tag', 'module', 'gen_location', 'severity', 'group', 'description', 'set_time', 'state', 'reporting_agent_id', 'resynced', 'detail_desc', 'clear_time'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_alarm_mgr as meta
                    return meta._meta_table['AlarmMgr.Detail.System.History']['meta_info']


            class Stats(_Entity_):
                """
                
                
                .. attribute:: attime  (key)
                
                	Alarms statistics at specified time
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: reported
                
                	Total alarms reported into this service
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: dropped
                
                	Alarms dropped due to some error or other
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: bi_set
                
                	Total active alarms current in this service
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: bi_clear
                
                	Alarms that are currently in the cleared state
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: suppressed
                
                	Alarms that are currently in the suppressed state
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: drop_inv_aid
                
                	Alarms dropped due to invalid aid in the alarm report
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: drop_no_mem
                
                	Alarms dropped due to low memory condition
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: drop_db_error
                
                	Alarms dropped due to database internal error
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: drop_clear_no_set
                
                	Alarms dropped due to clear without a set
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: drop_dup
                
                	Alarms dropped due to duplicate alarm report
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: cache_hit
                
                	Alarms present in the cached for show
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: cache_miss
                
                	Alarms not present in the cached for show
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                

                """

                _prefix = 'alarms'
                _revision = '2018-04-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(AlarmMgr.Detail.System.Stats, self).__init__()

                    self.yang_name = "stats"
                    self.yang_parent_name = "system"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['attime']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('attime', (YLeaf(YType.str, 'attime'), ['str'])),
                        ('reported', (YLeaf(YType.uint64, 'reported'), ['int'])),
                        ('dropped', (YLeaf(YType.uint64, 'dropped'), ['int'])),
                        ('bi_set', (YLeaf(YType.uint64, 'bi_set'), ['int'])),
                        ('bi_clear', (YLeaf(YType.uint64, 'bi_clear'), ['int'])),
                        ('suppressed', (YLeaf(YType.uint64, 'suppressed'), ['int'])),
                        ('drop_inv_aid', (YLeaf(YType.uint64, 'drop_inv_aid'), ['int'])),
                        ('drop_no_mem', (YLeaf(YType.uint64, 'drop_no_mem'), ['int'])),
                        ('drop_db_error', (YLeaf(YType.uint64, 'drop_db_error'), ['int'])),
                        ('drop_clear_no_set', (YLeaf(YType.uint64, 'drop_clear_no_set'), ['int'])),
                        ('drop_dup', (YLeaf(YType.uint64, 'drop_dup'), ['int'])),
                        ('cache_hit', (YLeaf(YType.uint64, 'cache_hit'), ['int'])),
                        ('cache_miss', (YLeaf(YType.uint64, 'cache_miss'), ['int'])),
                    ])
                    self.attime = None
                    self.reported = None
                    self.dropped = None
                    self.bi_set = None
                    self.bi_clear = None
                    self.suppressed = None
                    self.drop_inv_aid = None
                    self.drop_no_mem = None
                    self.drop_db_error = None
                    self.drop_clear_no_set = None
                    self.drop_dup = None
                    self.cache_hit = None
                    self.cache_miss = None
                    self._segment_path = lambda: "stats" + "[attime='" + str(self.attime) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-alarm-mgr:alarm_mgr/detail/system/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AlarmMgr.Detail.System.Stats, ['attime', 'reported', 'dropped', 'bi_set', 'bi_clear', 'suppressed', 'drop_inv_aid', 'drop_no_mem', 'drop_db_error', 'drop_clear_no_set', 'drop_dup', 'cache_hit', 'cache_miss'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_alarm_mgr as meta
                    return meta._meta_table['AlarmMgr.Detail.System.Stats']['meta_info']


            class Clients(_Entity_):
                """
                
                
                .. attribute:: agent_handle  (key)
                
                	The client handle through which interface
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: agent_name
                
                	Alarms client
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: agent_id
                
                	Alarms agent id of the client
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: agent_location
                
                	The location of this client
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: agent_state
                
                	The current state of the client
                	**type**\:  :py:class:`AgentStateTd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.AgentStateTd>`
                
                	**config**\: False
                
                .. attribute:: agent_type
                
                	The type of  the client
                	**type**\:  :py:class:`AgentTypeTd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.AgentTypeTd>`
                
                	**config**\: False
                
                .. attribute:: agent_filter_disp
                
                	The current subscription status of the client
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: agent_subs_id
                
                	The subscriber id of the client
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: agent_filter_state
                
                	The filter used for alarm bi\-state state
                	**type**\:  :py:class:`StatusTd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.StatusTd>`
                
                	**config**\: False
                
                .. attribute:: agent_filter_severity
                
                	The filter used for alarm severity
                	**type**\:  :py:class:`SeverityTd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.SeverityTd>`
                
                	**config**\: False
                
                .. attribute:: agent_filter_group
                
                	The filter used for alarm group
                	**type**\:  :py:class:`GroupTd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.GroupTd>`
                
                	**config**\: False
                
                .. attribute:: agent_sdr_id
                
                	agent alarm\_sm register with sdr\_id in SOMT mode
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: agent_connect_count
                
                	Number of times the agent connected to the alarm mgr
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: agent_connect_time
                
                	Agent connect timestamp
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: agent_get_count
                
                	Number of times the agent queried for alarms
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: agent_subscribe_count
                
                	Number of times the agent subscribed for alarms
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: agent_report_count
                
                	Number of times the agent reported alarms
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                

                """

                _prefix = 'alarms'
                _revision = '2018-04-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(AlarmMgr.Detail.System.Clients, self).__init__()

                    self.yang_name = "clients"
                    self.yang_parent_name = "system"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['agent_handle']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('agent_handle', (YLeaf(YType.str, 'agent_handle'), ['str'])),
                        ('agent_name', (YLeaf(YType.str, 'agent_name'), ['str'])),
                        ('agent_id', (YLeaf(YType.uint32, 'agent_id'), ['int'])),
                        ('agent_location', (YLeaf(YType.str, 'agent_location'), ['str'])),
                        ('agent_state', (YLeaf(YType.enumeration, 'agent_state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr', 'AgentStateTd', '')])),
                        ('agent_type', (YLeaf(YType.enumeration, 'agent_type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr', 'AgentTypeTd', '')])),
                        ('agent_filter_disp', (YLeaf(YType.boolean, 'agent_filter_disp'), ['bool'])),
                        ('agent_subs_id', (YLeaf(YType.uint32, 'agent_subs_id'), ['int'])),
                        ('agent_filter_state', (YLeaf(YType.enumeration, 'agent_filter_state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr', 'StatusTd', '')])),
                        ('agent_filter_severity', (YLeaf(YType.enumeration, 'agent_filter_severity'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr', 'SeverityTd', '')])),
                        ('agent_filter_group', (YLeaf(YType.enumeration, 'agent_filter_group'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr', 'GroupTd', '')])),
                        ('agent_sdr_id', (YLeaf(YType.uint32, 'agent_sdr_id'), ['int'])),
                        ('agent_connect_count', (YLeaf(YType.uint64, 'agent_connect_count'), ['int'])),
                        ('agent_connect_time', (YLeaf(YType.str, 'agent_connect_time'), ['str'])),
                        ('agent_get_count', (YLeaf(YType.uint64, 'agent_get_count'), ['int'])),
                        ('agent_subscribe_count', (YLeaf(YType.uint64, 'agent_subscribe_count'), ['int'])),
                        ('agent_report_count', (YLeaf(YType.uint64, 'agent_report_count'), ['int'])),
                    ])
                    self.agent_handle = None
                    self.agent_name = None
                    self.agent_id = None
                    self.agent_location = None
                    self.agent_state = None
                    self.agent_type = None
                    self.agent_filter_disp = None
                    self.agent_subs_id = None
                    self.agent_filter_state = None
                    self.agent_filter_severity = None
                    self.agent_filter_group = None
                    self.agent_sdr_id = None
                    self.agent_connect_count = None
                    self.agent_connect_time = None
                    self.agent_get_count = None
                    self.agent_subscribe_count = None
                    self.agent_report_count = None
                    self._segment_path = lambda: "clients" + "[agent_handle='" + str(self.agent_handle) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-alarm-mgr:alarm_mgr/detail/system/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AlarmMgr.Detail.System.Clients, ['agent_handle', 'agent_name', 'agent_id', 'agent_location', 'agent_state', 'agent_type', 'agent_filter_disp', 'agent_subs_id', 'agent_filter_state', 'agent_filter_severity', 'agent_filter_group', 'agent_sdr_id', 'agent_connect_count', 'agent_connect_time', 'agent_get_count', 'agent_subscribe_count', 'agent_report_count'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_alarm_mgr as meta
                    return meta._meta_table['AlarmMgr.Detail.System.Clients']['meta_info']


            class Suppressed(_Entity_):
                """
                
                
                .. attribute:: aid  (key)
                
                	The AID for the current alarm
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: eid  (key)
                
                	The Object Id for the current alarm
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: tag
                
                	The Fault Tag for the current alarm
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: module
                
                	The Module for the current alarm
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: gen_location
                
                	The location for the current alarm
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: severity
                
                	The alarm severity
                	**type**\:  :py:class:`SeverityTd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.SeverityTd>`
                
                	**config**\: False
                
                .. attribute:: group
                
                	The alarm grouping 
                	**type**\:  :py:class:`GroupTd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.GroupTd>`
                
                	**config**\: False
                
                .. attribute:: description
                
                	Alarm description
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: set_time
                
                	Alarm set time stamp
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: state
                
                	The current state of the bi\-state alarm
                	**type**\:  :py:class:`StatusTd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr.StatusTd>`
                
                	**config**\: False
                
                .. attribute:: reporting_agent_id
                
                	The reporting agent id
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: resynced
                
                	The condition bit\-flags of the alarm
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: detail_desc
                
                	Alarm detailed description
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: suppressed_time
                
                	Alarm suppressed time stamp
                	**type**\: str
                
                	**config**\: False
                
                

                """

                _prefix = 'alarms'
                _revision = '2018-04-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(AlarmMgr.Detail.System.Suppressed, self).__init__()

                    self.yang_name = "suppressed"
                    self.yang_parent_name = "system"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['aid','eid']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('aid', (YLeaf(YType.str, 'aid'), ['str'])),
                        ('eid', (YLeaf(YType.str, 'eid'), ['str'])),
                        ('tag', (YLeaf(YType.str, 'tag'), ['str'])),
                        ('module', (YLeaf(YType.str, 'module'), ['str'])),
                        ('gen_location', (YLeaf(YType.str, 'gen_location'), ['str'])),
                        ('severity', (YLeaf(YType.enumeration, 'severity'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr', 'SeverityTd', '')])),
                        ('group', (YLeaf(YType.enumeration, 'group'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr', 'GroupTd', '')])),
                        ('description', (YLeaf(YType.str, 'description'), ['str'])),
                        ('set_time', (YLeaf(YType.str, 'set_time'), ['str'])),
                        ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_alarm_mgr', 'StatusTd', '')])),
                        ('reporting_agent_id', (YLeaf(YType.uint32, 'reporting_agent_id'), ['int'])),
                        ('resynced', (YLeaf(YType.uint32, 'resynced'), ['int'])),
                        ('detail_desc', (YLeaf(YType.str, 'detail_desc'), ['str'])),
                        ('suppressed_time', (YLeaf(YType.str, 'suppressed_time'), ['str'])),
                    ])
                    self.aid = None
                    self.eid = None
                    self.tag = None
                    self.module = None
                    self.gen_location = None
                    self.severity = None
                    self.group = None
                    self.description = None
                    self.set_time = None
                    self.state = None
                    self.reporting_agent_id = None
                    self.resynced = None
                    self.detail_desc = None
                    self.suppressed_time = None
                    self._segment_path = lambda: "suppressed" + "[aid='" + str(self.aid) + "']" + "[eid='" + str(self.eid) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-alarm-mgr:alarm_mgr/detail/system/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AlarmMgr.Detail.System.Suppressed, ['aid', 'eid', 'tag', 'module', 'gen_location', 'severity', 'group', 'description', 'set_time', 'state', 'reporting_agent_id', 'resynced', 'detail_desc', 'suppressed_time'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_alarm_mgr as meta
                    return meta._meta_table['AlarmMgr.Detail.System.Suppressed']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_alarm_mgr as meta
                return meta._meta_table['AlarmMgr.Detail.System']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_alarm_mgr as meta
            return meta._meta_table['AlarmMgr.Detail']['meta_info']

    def clone_ptr(self):
        self._top_entity = AlarmMgr()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_alarm_mgr as meta
        return meta._meta_table['AlarmMgr']['meta_info']


