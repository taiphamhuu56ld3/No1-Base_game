"""
Some thing
"""

from typing import Any, Tuple, Optional


class Point2D():
    """
    Class point 2D
    """

    def __init__(self, arg: Optional[Any]) -> None:
        """_summary_
        """

        if arg is None:
            self.__x = 0.
            self.__y = 0.

        elif isinstance(arg, Point2D):
            self.__x = Point2D(self).X
            self.__y = Point2D(self).Y

        elif isinstance(arg, tuple):
            if len(arg) == 2:  # type: ignore
                self.__x = float(arg[0])  # type: ignore
                self.__y = float(arg[1])  # type: ignore

        else:
            self.__x = 0.
            self.__y = 0.

    def __repr__(self) -> str:
        return f"Point2D({self.__x}, {self.__y})"

    @property
    def X(self) -> float:
        return self.__x

    @X.setter
    def X(self, value: float):
        self.__x = value

    @property
    def Y(self) -> float:
        return self.__y

    @Y.setter
    def Y(self, value: float):
        self.__y = value


class Line2D():
    """
    Class line 2D
    """

    def __init__(self, *arg: Tuple[Any]) -> None:
        """_summary_
        """
        if arg is None:
            self.X1 = 0.
            self.Y1 = 0.
            self.X2 = 0.
            self.Y2 = 0.

        elif isinstance(arg, Line2D):
            self.X = Line2D().X
            self.Y = Line2D().Y

        elif isinstance(arg, Line2D):
            self.X = Line2D().X
            self.Y = Line2D().Y

        else:
            self.X = 0.
            self.Y = 0.

    @property
    def X(self) -> float:
        return self.X

    @X.setter
    def X(self, value: float):
        self.X = value

    @property
    def Y(self) -> float:
        return self.Y

    @Y.setter
    def Y(self, value: float):
        self.Y = value
