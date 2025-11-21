from typing import Optional, List
from dataclasses import dataclass


@dataclass
class Config:
    client_id: str
    access_token: str
    base_url: str = "https://www.lunartools.co"


@dataclass
class Thumbnail:
    url: Optional[str] = None


@dataclass
class Image:
    url: Optional[str] = None


@dataclass
class Footer:
    text: Optional[str] = None
    icon_url: Optional[str] = None


@dataclass
class Author:
    name: Optional[str] = None
    url: Optional[str] = None
    icon_url: Optional[str] = None


@dataclass
class Field:
    name: str
    value: str
    inline: Optional[bool] = None


@dataclass
class Embed:
    author: Optional[Author] = None
    title: Optional[str] = None
    url: Optional[str] = None
    description: Optional[str] = None
    color: Optional[int] = None
    fields: Optional[List[Field]] = None
    thumbnail: Optional[Thumbnail] = None
    image: Optional[Image] = None
    footer: Optional[Footer] = None
    timestamp: Optional[str] = None


@dataclass
class Webhook:
    username: Optional[str] = None
    avatar_url: Optional[str] = None
    content: Optional[str] = None
    embeds: Optional[List[Embed]] = None


@dataclass
class WebhookResponse:
    status: str
    queue_length: int


@dataclass
class AddProduct:
    name: str
    sku: str
    qty: int
    size: Optional[str] = None
    store: Optional[str] = None
    value: Optional[float] = None
    spent: Optional[float] = None


@dataclass
class AddOrder:
    name: str
    status: str
    order_number: str
    image: Optional[str] = None
    tracking: Optional[str] = None
    date: Optional[str] = None
    qty: Optional[str] = None
    price: Optional[str] = None
    order_total: Optional[str] = None
    account: Optional[str] = None
    retailer: Optional[str] = None
    tags: Optional[str] = None