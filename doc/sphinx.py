def parse_raw_temps(original_temps: TextIO,
                    step_size: int=30, units: bool=True) -> Iterator[Tuple[float, List[float]] ]:
    """
    Take an input file and time-step size and parse all core temps.

    Args:
        original_temps: an input file
        step_size: time-step in seconds
        units: True if the input file includes units and False if the file
            includes only raw readings (no units)

    Yields:
        A tuple containing the next time step and a List containing _n_
        core temps as floating point values (where _n_ is the number of
        CPU cores)
    """