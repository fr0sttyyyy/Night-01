import asyncio
from playwright.async_api import async_playwright, TimeoutError

ANSWER = "A"

accounts = [







{"username": "lul-78", "wallet": "D626hvrCbq13oPz8jZYdvNac28KM8bexirwCPtSBRjG4"},
{"username": "lul-79", "wallet": "3e1XfWpmRVfQSNeV1d298Cp9N83xYm2g2fuPAFS4wX5n"},
{"username": "lul-80", "wallet": "6oaYEYjefo9YMgsDg6riKM8uGLrbyhNthZ7kzxTDfpzM"},
{"username": "lul-81", "wallet": "4qX9CRm3TQP87sAd13Q3RN2mE1cTBFxdHUgH5ZuyPVfs"},
{"username": "lul-82", "wallet": "7CanuaFxHRzBw9DV9LiZknn1iYg1VdRhmmpa7ok3Ai6t"},
{"username": "lul-83", "wallet": "5FmJWocEYHNU6Wv2TDcuNMgDsbjCdksd4XUSruePTtH"},
{"username": "lul-84", "wallet": "BgmNdVAgFGcnrkroDQKAPPAWsgJNm5K8ffYSsCspd1W6"},
{"username": "lul-85", "wallet": "HCeA4Nzf1qz1hBrQLDcNw1d3dg1HTXoa91xskCT9i7AT"},
{"username": "lul-86", "wallet": "HC3not3A2WpzRA9psLaxh7H4bNtcxNRtm2PBJtWsz1jc"},
{"username": "lul-87", "wallet": "HTgNhevAJFYd7Lh5sFXhgDuVowhuZaQRdztcgcPtGWm9"},
{"username": "lul-88", "wallet": "4QqzKhPQQoWRha9JSLtDKViwZcYweE4n6Ru15CjVkkFj"},
{"username": "lul-89", "wallet": "7cuuSdZvhMSzf1cecScyTHryso213JWEGmi4bi7C8Aw4"},
{"username": "lul-90", "wallet": "4b3TsqWbG7FgHfipVRadd2ANQa1gPUTYdSnRWLbXNbFz"},
{"username": "lul-91", "wallet": "PwRkHekSeBQkqeNTMM9a4Sbz4gS6kbnur1sPUAFkqNp"},
{"username": "lul-92", "wallet": "6hwf6RJT5kAPNWELkbvoNjXvzm5WafhFXXechACisdXk"},
{"username": "lul-93", "wallet": "87JkhHJyNCySQsMeTub6LAkWYL7YBz8BqTCSmAbzdBNU"},
{"username": "lul-94", "wallet": "D9XydApNEYmqpR6FmxjhhzazB3bZnLyTnhcBnhGyS1Nx"},
{"username": "lul-95", "wallet": "3W1Yg6RXaetSCGrw9EVfomaRASFFgstWAxQEMBhCduSh"},
{"username": "lul-96", "wallet": "2GFNPQdXJFUrbTNQ4tBAe6pXX5MwUEsoKmjkDh1NyPPr"},
{"username": "lul-97", "wallet": "HH4bhknVTDd5BRMht7Gb8CoJPcn34YV3fAQPEgrGhnUP"},
{"username": "lul-98", "wallet": "3WypuKfc7BovSjDjpPnvFdWh8DwUAPK3YbHiMP9sL2yV"},
{"username": "lul-99", "wallet": "D284ZwpCrZqXF2YHBfNN9nBuxPZ2zj3C5vhT4ofLU18w"},
{"username": "lul-100", "wallet": "FDHFj9zFShZ7kxa2aR2rzkLVAWngbaCp2b1ebZq59dki"},

{"username": "NS-28", "wallet": "9vorrffuPHu9UTGJHbUxWW1HUuUBTbd7hBX5Z6kbdrjK"},









    
]


async def handle_modal(page):
    modal = page.locator("#scamMigrationWarningModal")
    try:
        if await modal.is_visible(timeout=5000):
            print("⚠️ Closing modal...")
            buttons = modal.locator("button")
            if await buttons.count() > 0:
                await buttons.first.click()
                await page.wait_for_timeout(1000)
    except Exception:
        pass


async def run_bot():
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            args=["--no-sandbox", "--disable-dev-shm-usage"],
        )

        for acc in accounts:
            context = await browser.new_context()
            page = await context.new_page()

            print("Running account:", acc["username"])

            try:
                await page.goto("https://theros.io/prelaunch", timeout=80000)
                await page.wait_for_load_state("networkidle", timeout=15000)
            except Exception as e:
                print(f"Connection error for {acc['username']}: {e}. Skipping account.")
                await context.close()
                continue

            await handle_modal(page)
            await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            await page.wait_for_selector("input", timeout=15000)

            inputs = await page.query_selector_all("input")
            if len(inputs) < 2:
                print(f"Not enough inputs for {acc['username']}, skipping")
                await context.close()
                continue

            await inputs[0].fill(acc["username"])
            await inputs[1].fill(acc["wallet"])

            if len(inputs) > 2:
                await inputs[2].fill("bot")

            await handle_modal(page)

            create_btn = page.locator("#registerBtn")
            try:
                await create_btn.click(timeout=9000)
            except TimeoutError:
                await create_btn.click(force=True)

            next_btn = page.locator("#nextQuestionBtn")
            try:
                await next_btn.wait_for(state="visible", timeout=8000)
                await next_btn.click()
            except Exception:
                pass

            answer_selector = f"#answer{ANSWER.upper()}"
            try:
                await page.locator(answer_selector).click(timeout=20000)
                print("Answered:", ANSWER)
            except Exception as e:
                print(f"Failed to answer: {e}")

            await page.wait_for_timeout(1000)
            await context.close()

        await browser.close()
        print("🎉 All accounts processed successfully!")


if __name__ == "__main__":
    asyncio.run(run_bot())
  
