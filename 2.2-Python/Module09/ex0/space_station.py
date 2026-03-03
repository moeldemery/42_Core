from datetime import datetime
from typing import Optional


try:
    from pydantic import BaseModel, Field, ValidationError

    DOTENV_AVAILABLE = True
except ImportError:
    DOTENV_AVAILABLE = False

if not DOTENV_AVAILABLE:
    print("WARNING: pydantic is not installed.")
    print("  Install it with: pip install pydantic")
    print("  Or with Poetry: poetry add pydantic")
    exit(1)


class SpaceStation(BaseModel):
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(default=None, max_length=200)

    def print_status(self):
        status = f"ID: {self.station_id}\n"
        status += f"Name: {self.name}\n"
        status += f"Crew Size: {self.crew_size} people\n"
        status += f"Power Level: {self.power_level}%\n"
        status += f"Oxygen Level: {self.oxygen_level}%\n"
        status += f"Last Maintenance: {self.last_maintenance}\n"
        if self.is_operational:
            status += "Status: Operational\n"
        else:
            status += "Status: Non-Operational\n"
        if self.notes:
            status += f"Notes: {self.notes}\n"

        print(status)


def main():
    print("Space Station Data Validation")
    print("="*30)

    try:
        station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime(2024, 1, 15, 8, 30, 0),
            is_operational=True,
            notes="All systems nominal.",
        )
        print("Valid station created:")
        station.print_status()
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(error["msg"])

    print("="*30)

    try:
        bad_station = SpaceStation(
            station_id="ISS002",
            name="Overcrowded Station",
            crew_size=25,
            power_level=1170.0,
            oxygen_level=80.0,
            last_maintenance=datetime(2024, 5, 1),
        )
        print("This should not print, data is invalid:")
        bad_station.print_status()
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(error["msg"])


if __name__ == "__main__":
    main()
