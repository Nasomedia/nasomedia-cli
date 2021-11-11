from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from app.db import Base

# from typing import TYPE_CHECKING
# if TYPE_CHECKING:
#     from .other import OtherTable
# from .other import OtherTable

class ModelFrame(Base):
    __tablename__ = "test_model"
    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    created_at = Column(DateTime(timezone=True), nullable=False)

    # 다대일 관계 형성
    # other_id = Column(Integer, ForeignKey(
    #     "other.id", ondelete="CASCADE"), nullable=True)
    # other = relationship(OtherTable)