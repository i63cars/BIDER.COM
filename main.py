
        from fastapi import FastAPI

        app = FastAPI()

        @app.get("/auctions")
        def get_auctions():
            return [{"id": 1, "name": "Luxury Car Auction"}]

        