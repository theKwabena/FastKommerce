from sqlalchemy import Column, String, Integer,ForeignKey
from sqlalchemy.orm import relationship

from config.settings import  Base


class Category(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255))

    products = relationship("Product", back_populates="category")


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key = True, index=True, autoincrement=True)
    name = Column(String(255))
    quantity = Column(Integer)
    description = Column(String)
    category_id = Column(Integer, ForeignKey("category.id", ondelete="CASCADE"))
    category = relationship("Category", back_populates="products")

    # order_details = relationship("OrderDetails", back_populates="product_order_details")
    # cart_items = relationship("CartItems", back_populates="products")