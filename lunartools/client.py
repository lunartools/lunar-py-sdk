import requests
from typing import Optional, Dict, Any


class Client:
    def __init__(self, client_id: str, access_token: str, base_url: str = "https://www.lunartools.co"):
        self.client_id = client_id
        self.access_token = access_token
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "X-Client-ID": client_id,
            "X-Access-Token": access_token
        })

    def add_product(
        self,
        name: str,
        sku: str,
        qty: int,
        size: Optional[str] = None,
        store: Optional[str] = None,
        value: Optional[float] = None,
        spent: Optional[float] = None
    ) -> None:
        if not name or not name.strip():
            raise ValueError("Product name is required")
        if not sku or not sku.strip():
            raise ValueError("Product SKU is required")
        if qty < 0:
            raise ValueError("Product quantity must be a non-negative number")
        if value is not None and value < 0:
            raise ValueError("Product value must be a non-negative number")
        if spent is not None and spent < 0:
            raise ValueError("Product spent must be a non-negative number")

        payload = {
            "clientId": self.client_id,
            "accessToken": self.access_token,
            "name": name,
            "sku": sku,
            "qty": qty
        }

        if size is not None:
            payload["size"] = size
        if store is not None:
            payload["store"] = store
        if value is not None:
            payload["value"] = value
        if spent is not None:
            payload["spent"] = spent

        response = self.session.post(f"{self.base_url}/sdk/add-product", json=payload)
        response.raise_for_status()

    def add_order(
        self,
        name: str,
        status: str,
        order_number: str,
        image: Optional[str] = None,
        tracking: Optional[str] = None,
        date: Optional[str] = None,
        qty: Optional[str] = None,
        price: Optional[str] = None,
        order_total: Optional[str] = None,
        account: Optional[str] = None,
        retailer: Optional[str] = None,
        tags: Optional[str] = None
    ) -> None:
        if not name or not name.strip():
            raise ValueError("Order name is required")
        if not status or not status.strip():
            raise ValueError("Order status is required")
        if not order_number or not order_number.strip():
            raise ValueError("Order number is required")

        payload = {
            "clientId": self.client_id,
            "accessToken": self.access_token,
            "name": name,
            "status": status,
            "orderNumber": order_number
        }

        if image is not None:
            payload["image"] = image
        if tracking is not None:
            payload["tracking"] = tracking
        if date is not None:
            payload["date"] = date
        if qty is not None:
            payload["qty"] = qty
        if price is not None:
            payload["price"] = price
        if order_total is not None:
            payload["orderTotal"] = order_total
        if account is not None:
            payload["account"] = account
        if retailer is not None:
            payload["retailer"] = retailer
        if tags is not None:
            payload["tags"] = tags

        response = self.session.post(f"{self.base_url}/sdk/add-order", json=payload)
        response.raise_for_status()

    def webhook(self, webhook_url: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        has_content = payload.get("content") and payload["content"].strip()
        has_embeds = payload.get("embeds") and len(payload["embeds"]) > 0

        if not has_content and not has_embeds:
            raise ValueError("Webhook payload must contain either content or at least one embed")
        
        if payload.get("embeds") and len(payload["embeds"]) > 10:
            raise ValueError("Discord webhooks support a maximum of 10 embeds")

        if payload.get("embeds"):
            for i, embed in enumerate(payload["embeds"]):
                if embed.get("fields") and len(embed["fields"]) > 25:
                    raise ValueError(f"Embed {i} exceeds the maximum of 25 fields")
                
                if embed.get("fields"):
                    for j, field in enumerate(embed["fields"]):
                        if not field.get("name") or not field["name"].strip():
                            raise ValueError(f"Embed {i}, field {j}: name is required")
                        if not field.get("value") or not field["value"].strip():
                            raise ValueError(f"Embed {i}, field {j}: value is required")

        response = requests.post(webhook_url, json=payload)
        response.raise_for_status()
        return response.json()