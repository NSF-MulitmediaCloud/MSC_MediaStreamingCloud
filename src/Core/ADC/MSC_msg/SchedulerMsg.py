# automatically generated by the FlatBuffers compiler, do not modify

# namespace: MSC_msg

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class SchedulerMsg(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = SchedulerMsg()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsSchedulerMsg(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # SchedulerMsg
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # SchedulerMsg
    def Operation(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int16Flags, o + self._tab.Pos)
        return 0

    # SchedulerMsg
    def ReturnDest(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # SchedulerMsg
    def Priority(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # SchedulerMsg
    def UserId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # SchedulerMsg
    def TaskId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # SchedulerMsg
    def TaskType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # SchedulerMsg
    def MachineType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # SchedulerMsg
    def ArrayTag(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # SchedulerMsg
    def Arr(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Float64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # SchedulerMsg
    def ArrAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Float64Flags, o)
        return 0

    # SchedulerMsg
    def ArrLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # SchedulerMsg
    def ArrIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        return o == 0

    # SchedulerMsg
    def MiscData(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def Start(builder): builder.StartObject(10)
def SchedulerMsgStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddOperation(builder, operation): builder.PrependInt16Slot(0, operation, 0)
def SchedulerMsgAddOperation(builder, operation):
    """This method is deprecated. Please switch to AddOperation."""
    return AddOperation(builder, operation)
def AddReturnDest(builder, returnDest): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(returnDest), 0)
def SchedulerMsgAddReturnDest(builder, returnDest):
    """This method is deprecated. Please switch to AddReturnDest."""
    return AddReturnDest(builder, returnDest)
def AddPriority(builder, priority): builder.PrependInt8Slot(2, priority, 0)
def SchedulerMsgAddPriority(builder, priority):
    """This method is deprecated. Please switch to AddPriority."""
    return AddPriority(builder, priority)
def AddUserId(builder, userId): builder.PrependInt64Slot(3, userId, 0)
def SchedulerMsgAddUserId(builder, userId):
    """This method is deprecated. Please switch to AddUserId."""
    return AddUserId(builder, userId)
def AddTaskId(builder, taskId): builder.PrependInt64Slot(4, taskId, 0)
def SchedulerMsgAddTaskId(builder, taskId):
    """This method is deprecated. Please switch to AddTaskId."""
    return AddTaskId(builder, taskId)
def AddTaskType(builder, taskType): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(taskType), 0)
def SchedulerMsgAddTaskType(builder, taskType):
    """This method is deprecated. Please switch to AddTaskType."""
    return AddTaskType(builder, taskType)
def AddMachineType(builder, machineType): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(machineType), 0)
def SchedulerMsgAddMachineType(builder, machineType):
    """This method is deprecated. Please switch to AddMachineType."""
    return AddMachineType(builder, machineType)
def AddArrayTag(builder, arrayTag): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(arrayTag), 0)
def SchedulerMsgAddArrayTag(builder, arrayTag):
    """This method is deprecated. Please switch to AddArrayTag."""
    return AddArrayTag(builder, arrayTag)
def AddArr(builder, arr): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(arr), 0)
def SchedulerMsgAddArr(builder, arr):
    """This method is deprecated. Please switch to AddArr."""
    return AddArr(builder, arr)
def StartArrVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def SchedulerMsgStartArrVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartArrVector(builder, numElems)
def AddMiscData(builder, miscData): builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(miscData), 0)
def SchedulerMsgAddMiscData(builder, miscData):
    """This method is deprecated. Please switch to AddMiscData."""
    return AddMiscData(builder, miscData)
def End(builder): return builder.EndObject()
def SchedulerMsgEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)