# This Python file uses the following encoding: utf-8
from enum import Enum
from PyQt5.QtCore import QObject, pyqtProperty, pyqtSignal, QVariant
from model.Utilities import formatPath


class GeneralSettings(QObject):
    _numTrajectories = 1000
    _populationPath = ""
    _detectionMildProbability = 0.3
    _stopSimulationThreshold = 10000

    numTrajectoriesChanged = pyqtSignal()
    populationPathChanged = pyqtSignal()
    detectionMildProbabilityChanged = pyqtSignal()
    stopSimulationThresholdChanged = pyqtSignal()

    class Properties(Enum):
        NumTrajectories = 'num_trajectories'
        PopulationPath = 'population_path'
        DetectionMildProbability = 'detection_mild_proba'
        StopSimulationThreshold = 'stop_simulation_threshold'

    @pyqtProperty(int, notify=numTrajectoriesChanged)
    def numTrajectories(self):
        return self._numTrajectories

    @pyqtProperty(str, notify=populationPathChanged)
    def populationPath(self):
        return self._populationPath

    @pyqtProperty(float, notify=detectionMildProbabilityChanged)
    def detectionMildProbability(self):
        return self._detectionMildProbability

    @pyqtProperty(int, notify=stopSimulationThresholdChanged)
    def stopSimulationThreshold(self):
        return self._stopSimulationThreshold

    @numTrajectories.setter
    def numTrajectories(self, val):
        if self._numTrajectories != val:
            self._numTrajectories = val
            self.numTrajectoriesChanged.emit()

    @populationPath.setter
    def populationPath(self, path):
        path = formatPath(path)
        if self._populationPath != path:
            self._populationPath = path
            self.populationPathChanged.emit()

    @detectionMildProbability.setter
    def detectionMildProbability(self, val):
        if self._detectionMildProbability != val:
            self._detectionMildProbability = val
            self.detectionMildProbabilityChanged.emit()

    @stopSimulationThreshold.setter
    def stopSimulationThreshold(self, val):
        if self._stopSimulationThreshold != val:
            self._stopSimulationThreshold = val
            self.stopSimulationThresholdChanged.emit()

    def serialize(self):
        return {
            self.Properties.NumTrajectories.value: self._numTrajectories,
            self.Properties.PopulationPath.value: self._populationPath,
            self.Properties.DetectionMildProbability.value: self._detectionMildProbability,
            self.Properties.StopSimulationThreshold.value: self._stopSimulationThreshold
        }


class ContactTracking(QObject):
    _probability = 0.5
    _backwardDetectionDelay = 1.75
    _forwardDetectionDelay = 1.75
    _testingTime = 0.25

    probabilityChanged = pyqtSignal()
    backwardDetectionDelayChanged = pyqtSignal()
    forwardDetectionDelayChanged = pyqtSignal()
    testingTimeChanged = pyqtSignal()

    class Properties(Enum):
        Probability = 'probability'
        BackwardDetectionDelay = 'backward_detection_delay'
        ForwardDetectionDelay = 'forward_detection_delay'
        TestingTime = 'testing_time'

    @staticmethod
    def description():
        return 'contact_tracking'

    @pyqtProperty(float, notify=probabilityChanged)
    def probability(self):
        return self._probability

    @pyqtProperty(float, notify=backwardDetectionDelayChanged)
    def backwardDetectionDelay(self):
        return self._backwardDetectionDelay

    @pyqtProperty(float, notify=forwardDetectionDelayChanged)
    def forwardDetectionDelay(self):
        return self._forwardDetectionDelay

    @pyqtProperty(float, notify=testingTimeChanged)
    def testingTime(self):
        return self._testingTime

    @probability.setter
    def probability(self, val):
        if self._probability != val:
            self._probability = val
            self.probabilityChanged.emit()

    @backwardDetectionDelay.setter
    def backwardDetectionDelay(self, val):
        if self._backwardDetectionDelay != val:
            self._backwardDetectionDelay = val
            self.backwardDetectionDelayChanged.emit()

    @forwardDetectionDelay.setter
    def forwardDetectionDelay(self, val):
        if self._forwardDetectionDelay != val:
            self._forwardDetectionDelay = val
            self.forwardDetectionDelayChanged.emit()

    @testingTime.setter
    def testingTime(self, val):
        if self._testingTime == val:
            return
        self._testingTime = val
        self.testingTimeChanged.emit()

    def serialize(self):
        return {
            self.Properties.Probability.value: self._probability,
            self.Properties.BackwardDetectionDelay.value: self._backwardDetectionDelay,
            self.Properties.ForwardDetectionDelay.value: self._forwardDetectionDelay,
            self.Properties.TestingTime.value: self._testingTime
        }


class TransmissionProbabilities(QObject):
    _household = 0.3
    _constant = 1.35
    _hospital = 0.0
    _friendship = 0.0
    _isHouseholdKernelEnabled = _household != 0.0
    _isConstantKernelEnabled = _constant != 0.0
    _isHospitalKernelEnabled = _hospital != 0.0
    _isFriendshipKernelEnabled = _friendship != 0.0

    householdChanged = pyqtSignal()
    constantChanged = pyqtSignal()
    hospitalChanged = pyqtSignal()
    friendshipChanged = pyqtSignal()

    householdKernelEnabledChanged = pyqtSignal()
    constantKernelEnabledChanged = pyqtSignal()
    hospitalKernelEnabledChanged = pyqtSignal()
    friendshipKernelEnabledChanged = pyqtSignal()

    class Properties(Enum):
        Household = 'household'
        Constant = 'constant'
        Hospital = 'hospital'
        Friendship = 'friendship'

    @staticmethod
    def description():
        return 'transmission_probabilities'

    @pyqtProperty(float, notify=householdChanged)
    def household(self):
        return self._household

    @pyqtProperty(float, notify=constantChanged)
    def constant(self):
        return self._constant

    @pyqtProperty(float, notify=hospitalChanged)
    def hospital(self):
        return self._hospital

    @pyqtProperty(float, notify=friendshipChanged)
    def friendship(self):
        return self._friendship

    @pyqtProperty(bool, notify=constantKernelEnabledChanged)
    def isHouseholdKernelEnabled(self):
        return self._isHouseholdKernelEnabled

    @pyqtProperty(bool, notify=constantKernelEnabledChanged)
    def isConstantKernelEnabled(self):
        return self._isConstantKernelEnabled

    @pyqtProperty(bool, notify=hospitalKernelEnabledChanged)
    def isHospitalKernelEnabled(self):
        return self._isHospitalKernelEnabled

    @pyqtProperty(bool, notify=friendshipKernelEnabledChanged)
    def isFriendshipKernelEnabled(self):
        return self._isFriendshipKernelEnabled

    @household.setter
    def household(self, val):
        if self._household != val:
            self._household = val
            self.householdChanged.emit()

    @constant.setter
    def constant(self, val):
        if self._constant != val:
            self._constant = val
            self.constantChanged.emit()

    @hospital.setter
    def hospital(self, val):
        if self._hospital != val:
            self._hospital = val
            self.hospitalChanged.emit()

    @friendship.setter
    def friendship(self, val):
        if self._friendship != val:
            self._friendship = val
            self.friendshipChanged.emit()

    @isHouseholdKernelEnabled.setter
    def isHouseholdKernelEnabled(self, value):
        if self._isHouseholdKernelEnabled != value:
            self._isHouseholdKernelEnabled = value
            self.householdKernelEnabledChanged.emit()

    @isConstantKernelEnabled.setter
    def isConstantKernelEnabled(self, value):
        if self._isConstantKernelEnabled != value:
            self._isConstantKernelEnabled = value
            self.constantKernelEnabledChanged.emit()

    @isHospitalKernelEnabled.setter
    def isHospitalKernelEnabled(self, value):
        if self._isHospitalKernelEnabled != value:
            self._isHospitalKernelEnabled = value
            self.hospitalKernelEnabledChanged.emit()

    @isFriendshipKernelEnabled.setter
    def isFriendshipKernelEnabled(self, value):
        if self._isFriendshipKernelEnabled != value:
            self._isFriendshipKernelEnabled = value
            self.friendshipKernelEnabledChanged.emit()

    def serialize(self):
        return {
            self.Properties.Household.value: self._household if self._isHouseholdKernelEnabled else 0.0,
            self.Properties.Constant.value: self._constant if self._isConstantKernelEnabled else 0.0,
            self.Properties.Hospital.value: self._hospital if self._isHospitalKernelEnabled else 0.0,
            self.Properties.Friendship.value: self._friendship if self._isFriendshipKernelEnabled else 0.0
        }


class ModulationFunctions(Enum):
    NONE = "None"
    TANH = "TanhModulation"

    @staticmethod
    def values():
        res = []
        for f in ModulationFunctions:
            res.append(f.value)
        return res

    @staticmethod
    def from_value(value):
        for funcType in ModulationFunctions:
            if value == funcType.value:
                return funcType
        raise NotImplementedError


class ValueTypes(Enum):
    PositiveIntegerValue = 0
    PositiveDoubleValue = 1
    InfiniteDoubleValue = 2


class ModulationParams:
    _properties = []
    _values = []
    _valueTypes = []

    def serialize(self):
        result = {}
        for i in range(0, len(self._properties)):
            result[self._properties[i].lower().replace(" ", "_")] = self._values[i]
        return result


class EmptyModulationParams(ModulationParams):
    def __init__(self):
        super().__init__()


class TanhModulationParams(ModulationParams):
    class Properties(Enum):
        Scale = 'scale'
        Loc = 'loc'
        WeightDetected = 'weight_detected'
        WeightDeaths = 'weight_deaths'
        LimitValue = 'limit_value'

    def __init__(self):
        self._properties = ["Scale", "Loc", "Weight detected", "Weight deaths", "Limit value"]
        self._values = [2000.0, 500.0, 1.0, 0.0, 0.5]
        self._valueTypes = [
            ValueTypes.PositiveDoubleValue,
            ValueTypes.InfiniteDoubleValue,
            ValueTypes.PositiveDoubleValue,
            ValueTypes.PositiveDoubleValue,
            ValueTypes.PositiveDoubleValue
        ]


class Modulation:
    _function = ModulationFunctions.NONE
    _emptyModulationParams = EmptyModulationParams()
    _tanhModulationParams = TanhModulationParams()

    class Properties(Enum):
        Function = 'function'
        Params = 'params'

    @staticmethod
    def description():
        return 'modulation'

    def getActiveParams(self):
        if self._function == ModulationFunctions.NONE:
            return self._emptyModulationParams
        elif self._function == ModulationFunctions.TANH:
            return self._tanhModulationParams
        raise NotImplementedError

    def serialize(self):
        assert(self._function != ModulationFunctions.NONE)
        return {
            self.Properties.Function.value: self._function.value,
            self.Properties.Params.value: self.getActiveParams().serialize()
        }


class Cardinalities(QObject):
    _infectious = 100

    infectiousChanged = pyqtSignal()

    @staticmethod
    def description(Enum):
        return 'cardinalities'

    class Properties(Enum):
        Infectious = 'infectious'

    @pyqtProperty(int, notify=infectiousChanged)
    def infectious(self):
        return self._infectious

    @infectious.setter
    def infectious(self, val):
        if self._infectious != val:
            self._infectious = val
            self.infectiousChanged.emit()

    def serialize(self):
        return {
            self.Properties.Infectious.value: self._infectious
        }


class InitialConditions(QObject):
    _cardinalities = Cardinalities()

    cardinalitiesChanged = pyqtSignal(QVariant, arguments=["value"])

    @staticmethod
    def description():
        return 'initial_conditions'

    class Properties(Enum):
        Cardinalities = 'cardinalities'

    @pyqtProperty(Cardinalities, notify=cardinalitiesChanged)
    def cardinalities(self):
        return self._cardinalities

    def serialize(self):
        return {
            self.Properties.Cardinalities.value: self._cardinalities.serialize()
        }


class PhoneTracking(QObject):
    _usage = 0.0
    _detectionDelay = 0.25
    _usageByHousehold = True

    usageChanged = pyqtSignal()
    detectionDelayChanged = pyqtSignal()
    usageByHouseholdChanged = pyqtSignal()

    class Properties(Enum):
        Usage = 'usage'
        DetectionDelay = 'detection_delay'
        UsageByHousehold = 'usage_by_household'

    @staticmethod
    def description():
        return 'phone_tracking'

    @pyqtProperty(float, notify=usageChanged)
    def usage(self):
        return self._usage

    @pyqtProperty(float, notify=detectionDelayChanged)
    def detectionDelay(self):
        return self._detectionDelay

    @pyqtProperty(bool, notify=usageByHouseholdChanged)
    def usageByHousehold(self):
        return self._usageByHousehold

    @usage.setter
    def usage(self, val):
        if self._usage != val:
            self._usage = val
            self.usageChanged.emit()

    @detectionDelay.setter
    def detectionDelay(self, val):
        if self._detectionDelay != val:
            self._detectionDelay = val
            self.detectionDelayChanged.emit()

    @usageByHousehold.setter
    def usageByHousehold(self, val):
        if self._usageByHousehold != val:
            self._usageByHousehold = val
            self.usageByHouseholdChanged.emit()

    def serialize(self):
        return {
            self.Properties.Usage.value: self._usage,
            self.Properties.DetectionDelay.value: self._detectionDelay,
            self.Properties.UsageByHousehold.value: self._usageByHousehold
        }


class Spreading(QObject):
    _alpha = 3.0
    _x0 = 1.0
    _truncation = 100.0

    alphaChanged = pyqtSignal()
    x0Changed = pyqtSignal()
    truncationChanged = pyqtSignal()
    truncationAcceptabilityCheckReq = pyqtSignal()

    class Properties(Enum):
        Alpha = 'alpha'
        X0 = 'x0'
        Truncation = 'truncation'

    @staticmethod
    def description():
        return 'spreading'

    @pyqtProperty(float, notify=alphaChanged)
    def alpha(self):
        return self._alpha

    @pyqtProperty(float, notify=x0Changed)
    def x0(self):
        return self._x0

    @pyqtProperty(float, notify=truncationChanged)
    def truncation(self):
        return self._truncation

    @alpha.setter
    def alpha(self, value):
        if self._alpha != value and value > 0.0:
            self._alpha = value
        self.alphaChanged.emit()

    @x0.setter
    def x0(self, value):
        if self._x0 != value and value > 0.0:
            self._x0 = value
        self.x0Changed.emit()
        self.truncationAcceptabilityCheckReq.emit()

    @truncation.setter
    def truncation(self, value):
        if self._truncation != value and value > 0.0:
            self._truncation = value
        self.truncationChanged.emit()
        self.truncationAcceptabilityCheckReq.emit()

    @pyqtProperty(bool, notify=truncationAcceptabilityCheckReq)
    def isTruncationAcceptable(self):
        return self._truncation > self._x0

    def serialize(self):
        return {
            self.Properties.Alpha.value: self._alpha,
            self.Properties.X0.value: self._x0,
            self.Properties.Truncation.value: self._truncation
        }


class SettingsSetter:
    @staticmethod
    def copySettingsFromJson(settings, jsonData):
        SettingsSetter._copyGeneralSettings(settings, jsonData)
        SettingsSetter._copyInitialConditions(settings, jsonData)
        SettingsSetter._copyContactTracking(settings, jsonData)
        SettingsSetter._copyModulationSettings(settings, jsonData)
        SettingsSetter._copyPhoneTracking(settings, jsonData)
        SettingsSetter._copyTransmissionProbabilities(settings, jsonData)
        SettingsSetter._copySpreading(settings, jsonData)

    @staticmethod
    def _copyGeneralSettings(settings, jsonData):
        gs = settings.generalSettings
        gs.numTrajectories = jsonData[GeneralSettings.Properties.NumTrajectories.value]
        gs.populationPath = jsonData[GeneralSettings.Properties.PopulationPath.value]
        gs.detectionMildProbability = jsonData[GeneralSettings.Properties.DetectionMildProbability.value]
        gs.stopSimulationThreshold = jsonData[GeneralSettings.Properties.StopSimulationThreshold.value]

    @staticmethod
    def _copyInitialConditions(settings, jsonData):
        ic = jsonData[InitialConditions.description()]
        cardinalities = ic[InitialConditions.Properties.Cardinalities.value]
        settings.initialConditions.cardinalities.infectious = cardinalities[Cardinalities.Properties.Infectious.value]

    @staticmethod
    def _copyContactTracking(settings, jsonData):
        ct = jsonData[ContactTracking.description()]
        settings.contactTracking.probability = ct[ContactTracking.Properties.Probability.value]
        settings.contactTracking.backwardDetectionDelay = ct[ContactTracking.Properties.BackwardDetectionDelay.value]
        settings.contactTracking.forwardDetectionDelay = ct[ContactTracking.Properties.ForwardDetectionDelay.value]
        settings.contactTracking.testingTime = ct[ContactTracking.Properties.TestingTime.value]

    @staticmethod
    def _copyModulationSettings(settings, jsonData):
        modulationSettings = jsonData.get(Modulation.description())
        if modulationSettings is None:
            settings.modulation._function = ModulationFunctions.NONE
            return
        functionType = modulationSettings.get(Modulation.Properties.Function.value)
        if functionType == ModulationFunctions.TANH.value:
            settings.modulation._function = ModulationFunctions.TANH
            jsonParams = modulationSettings[Modulation.Properties.Params.value]
            SettingsSetter._copyModulationFuncParams(settings.modulation._tanhModulationParams, jsonParams)
        else:
            raise NotImplementedError

    @staticmethod
    def _copyModulationFuncParams(functionParams, jsonData):
        i = 0
        for pr in functionParams.Properties:
            functionParams._values[i] = jsonData[pr.value]
            i += 1

    @staticmethod
    def _copyPhoneTracking(settings, jsonData):
        pt = jsonData[PhoneTracking.description()]
        settings.phoneTracking.usage = pt[PhoneTracking.Properties.Usage.value]
        settings.phoneTracking.detectionDelay = pt[PhoneTracking.Properties.DetectionDelay.value]
        settings.phoneTracking.usageByHousehold = pt[PhoneTracking.Properties.UsageByHousehold.value]

    @staticmethod
    def _copyTransmissionProbabilities(settings, jsonData):
        tp = jsonData[TransmissionProbabilities.description()]
        settings.transmissionProbabilities.household = tp[TransmissionProbabilities.Properties.Household.value]
        settings.transmissionProbabilities.constant = tp[TransmissionProbabilities.Properties.Constant.value]
        settings.transmissionProbabilities.hospital = tp[TransmissionProbabilities.Properties.Hospital.value]
        settings.transmissionProbabilities.friendship = tp[TransmissionProbabilities.Properties.Friendship.value]
        settings.transmissionProbabilities.isHouseholdKernelEnabled = settings.transmissionProbabilities.household != 0
        settings.transmissionProbabilities.isConstantKernelEnabled = settings.transmissionProbabilities.constant != 0
        settings.transmissionProbabilities.isHospitalKernelEnabled = settings.transmissionProbabilities.hospital != 0
        settings.transmissionProbabilities.isFriendshipKernelEnabled = settings.transmissionProbabilities.friendship != 0

    @staticmethod
    def _copySpreading(settings, jsonData):
        spr = jsonData[Spreading.description()]
        settings.spreading.alpha = spr[Spreading.Properties.Alpha.value]
        settings.spreading.x0 = spr[Spreading.Properties.X0.value]
        settings.spreading.truncation = spr[Spreading.Properties.Truncation.value]


class ProjectSettings:
    def __init__(self):
        self.initialConditions = InitialConditions()
        self.generalSettings = GeneralSettings()
        self.contactTracking = ContactTracking()
        self.transmissionProbabilities = TransmissionProbabilities()
        self.modulation = Modulation()
        self.phoneTracking = PhoneTracking()
        self.spreading = Spreading()

    def populate(self, jsonData):
        SettingsSetter.copySettingsFromJson(self, jsonData)

    def serialize(self):
        serialized = self.generalSettings.serialize()
        serialized[InitialConditions.description()] = self.initialConditions.serialize()
        serialized[Spreading.description()] = self.spreading.serialize()
        serialized[ContactTracking.description()] = self.contactTracking.serialize()
        serialized[TransmissionProbabilities.description()] = self.transmissionProbabilities.serialize()
        if (self.modulation._function != ModulationFunctions.NONE):
            serialized[Modulation.description()] = self.modulation.serialize()
        serialized[PhoneTracking.description()] = self.phoneTracking.serialize()
        return serialized
