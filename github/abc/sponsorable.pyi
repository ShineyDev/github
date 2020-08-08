from typing import Optional

from github.objects import SponsorListing


class Sponsorable():
    async def fetch_sponsor_listing(self) -> Optional[SponsorListing]: ...
