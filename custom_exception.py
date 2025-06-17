class ArgumentsException(Exception):
    """_summary_

    Args:
        Exception (_type_): _description_
    """

    def __init__(self, message, cli_argument):
        """_summary_

        Args:
            message (_type_): _description_
            cli_argument (_type_): _description_
        """
        super().__init__(message)
        self.message = message
        self.cli_argument = cli_argument
        

    def __str__(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return f'{self.message}, {self.cli_argument}'

