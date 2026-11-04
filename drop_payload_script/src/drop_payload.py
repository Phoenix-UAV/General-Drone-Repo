"""Drop payload script."""


def line_ab(a: float[3], b: float[3]) -> float[3]:
    """Find the line vector moving from point A to point B. Returns a line."""
    return [b[0] - a[0], b[1] - a[1], b[2] - a[2]]


def calculate_drop_position(
    plane_speed_mps: float,
    cardinal_angle_rad: float,
    windspeed_mps: float,
    wind_dir_rad: float,
    ground_normal: float[3],
    altitude_m: float,
) -> float[3]:
    """
    Calculate how far from the target the plane should drop the payload.

    Parameters:
    - plane_speed_mps: Current speed of the plane in meters per second.
    - cardinal_angle_rad: The cardinal angle of the plane in radians.
    - windspeed_mps: The windspeed in meters per second.
    - wind_dir_rad: The wind direction in radians.
    - ground_normal: The ground's normal vector at the target location.
    - altitude_m: The final altitude of the plane in meters.

    Returns a position the plane must have to drop the payload.
    """


def goto_point_with_direction(target_pos: float[3], target_dir: float[3]) -> None:
    """
    Tell the plane to go to a location facing some direction.

    Parameters:
    - target_pos: Target position.
    - target_dir: Target direction.
    """


def mission_drop_payload(
    windspeed_mps: float = 0.0,
    wind_dir_rad: float = 0.0,
    drop_gnd_normal: float[3] = [0, 0, 1],
):
    """
    Begin the payload drop script.

    Parameters:
    - windspeed_mps: Windspeed in meters per second.
    - wind_dir_rad: Wind direction in radians.
    - drop_gnd_normal: Ground normal at the dropoff location.
    """
    # get position

    # get direction

    # Align plane with target

    # Descend to reach calculated distance

    # 1. Determine from which distance from target to drop the water (consider windspeed probably and ground slope)
    # 2. Have plane move to some distance away from target position, facing the target
    # 3. Reduce altitude
    # 4. Deploy water at determined distance
    # 5. Regain former altitude
