import enum


@enum.unique
class MLFlowModelFlavor(str, enum.Enum):
    PYFUNC = "pyfunc"
    SKLEARN = "sklearn"
