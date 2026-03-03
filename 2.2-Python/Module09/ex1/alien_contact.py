
from datetime import datetime
from enum import Enum
from typing import Optional

try:
    from pydantic import BaseModel, Field, model_validator, ValidationError

    DOTENV_AVAILABLE = True
except ImportError:
    DOTENV_AVAILABLE = False

if not DOTENV_AVAILABLE:
    print("WARNING: pydantic is not installed.")
    print("  Install it with: pip install pydantic")
    print("  Or with Poetry: poetry add pydantic")
    exit(1)


class ContactType(str, Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(..., min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(..., min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(..., ge=0.0, le=10.0)
    duration_minutes: int = Field(..., ge=1, le=1440)
    witness_count: int = Field(..., ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def validate_contact_rules(self) -> "AlienContact":
        if not self.contact_id.startswith("AC"):
            raise ValueError('Contact ID must start with "AC"')

        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")

        if (
            self.contact_type == ContactType.telepathic
            and self.witness_count < 3
        ):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
            )

        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(
                "Strong signals (> 7.0) should include received messages"
            )

        return self

    def print_status(self):
        status = f"ID: {self.contact_id}\n"
        status += (f"Type: {self.contact_type.value}\n")
        status += (f"Location: {self.location}\n")
        status += (f"Signal: {self.signal_strength}/10\n")
        status += (f"Duration: {self.duration_minutes} minutes\n")
        status += (f"Witnesses: {self.witness_count}\n")
        if self.message_received:
            status += f"Message Received: {self.message_received}\n"
        status += f"Timestamp: {self.timestamp}\n"

        if self.is_verified:
            status += "Verified: Yes\n"
        else:
            status += "Verified: No\n"

        print(status)


def main() -> None:
    print("Alien Contact Log Validation")
    print("=" * 40)

    contact = AlienContact(
        contact_id="AC_2024_001",
        timestamp=datetime(2024, 6, 21, 14, 30, 0),
        location="Area 51, Nevada",
        contact_type=ContactType.radio,
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="Greetings from Zeta Reticuli",
        is_verified=True,
    )

    print("Valid contact report:")
    contact.print_status()

    print("=" * 40)

    try:
        faulted_contact = AlienContact(
            contact_id="AC_2024_002",
            timestamp=datetime(2024, 6, 21, 15, 0, 0),
            location="Roswell, New Mexico",
            contact_type=ContactType.telepathic,
            signal_strength=5.0,
            duration_minutes=20,
            witness_count=1,
        )
        faulted_contact.print_status()
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(error["msg"])


if __name__ == "__main__":
    main()
