from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class SubscriptionPlan(BaseModel):
    name: str
    price: float
    features: int
    description: Optional[str] = None


class SubscriptionCreate(BaseModel):
    plan: str = Field(..., max_length=50)

    class Config:
        json_schema_extra = {
            "example": {
                "plan": "pro"
            }
        }


class SubscriptionResponse(BaseModel):
    id: int
    user_id: int
    plan: str
    is_active: bool
    started_at: datetime
    expires_at: Optional[datetime]
    price: float
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class SubscriptionWithPlan(SubscriptionResponse):
    plan_name: str
    plan_features: int
