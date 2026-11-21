import asyncio
from playwright.async_api import async_playwright, TimeoutError

ANSWER = "A"

accounts = [









{"username":"Fossil-1","wallet":"2RcFLE1cagK8bkj345J8yZbTdSAwn6J59pXgXdxVvbLT"},
{"username":"Fossil-2","wallet":"9DvHS59hNgAUAi4z6hMv8symBXG3i9pMBs56gnDzYZU8"},
{"username":"Fossil-3","wallet":"2yi7zGK8jk7DJ9xm7tJYY1eN3YUDeZC1GfU3yZ4WSQej"},
{"username":"Fossil-4","wallet":"F7shjdmfdsLLASKzHoVCDJWqTcFyPnME1PmCBqSV6mjU"},
{"username":"Fossil-5","wallet":"BqsMU1o1abAhxfdP3Lqf8aL5BwdkJUQNwbNXf4gwdLiP"},
{"username":"Fossil-6","wallet":"8vCjQ7WLDmtsBq2nbWczPNaDC2A3wcqFVYu3fGY1GFiH"},
{"username":"Fossil-7","wallet":"LXiRsDpMkH2RFdC2okpEv3VKf7bjCtGotQ3AwwGKxMB"},
{"username":"Fossil-8","wallet":"LXiRsDpMkH2RFdC2okpEv3VKf7bjCtGotQ3AwwGKxMB"},
{"username":"Fossil-9","wallet":"BnR2zXTNiBbztiM4tYBXNV3PS8GPtHDis4ej9iuod7wk"},
{"username":"Fossil-10","wallet":"5TWhJukhVSUuHaZFSebW9EwCY9w4xQSD7weotNnoxF7W"},
{"username":"Fossil-11","wallet":"4pW6vs68B5X7uurtD1kRLMh2vRhYT4tReTL9iKse1APJ"},
{"username":"Fossil-12","wallet":"2Z89yW8awLx3gA99RZ9xP2mRYqRf4TeqLtJkM3SU5Baw"},
{"username":"Fossil-13","wallet":"Pyde1qwy2NwUSHBHk4FciqRTt7xwZcs7t5drDyAUn8p"},
{"username":"Fossil-14","wallet":"63naNabtvkJTdA7BiC5y3LiZmq4TQm7eGRzYuu5LTp3N"},
{"username":"Fossil-15","wallet":"BKXr18rqXhZuJxYbKGoQKF49rda8wKD3mhuc1xKo8sto"},
{"username":"Fossil-16","wallet":"8Tkm9pPGfNGbFRb6taSNWWdLpe43qevoKxNeyhaRRvT5"},
{"username":"Fossil-17","wallet":"CdsWFe1c4gRGxyBgFV4LSPzUwBjAhK6QSsF5SdP82ooM"},
{"username":"Fossil-18","wallet":"2w3ZsMJeqHogFkd6KrZmTRTc4aachcAqhJmK1ENLzUMf"},
{"username":"Fossil-19","wallet":"6ez77vrrwiuV6JJTAfgha69r653fNcU8WbKbCyYv8SEX"},
{"username":"Fossil-20","wallet":"AREBUwgBE65zzq4DmJ3FxJ7qGsYHZDtvDQe9DqjnLtXx"},
{"username":"Fossil-21","wallet":"6MTfVuZ6Ax37AnutL85rUPybDkgvNCLTSE8c9wTGYf2X"},
{"username":"Fossil-22","wallet":"GoK9wxbLV3L3zZtDTt6NrJRi75afmGCdob7ZQ1tmS5gD"},
{"username":"Fossil-23","wallet":"BZZp4BY2JaMNVVLhV8oy5fucVbczmpkfPV5mcEJHoqhe"},
{"username":"Fossil-24","wallet":"3pVzNkpbA17V9YHkuUnr9fdAy8r3FHB7Z3BKnTMWES3w"},
{"username":"Fossil-25","wallet":"HmUzo4UPWD24qkCMKRx23rT31RKG1BodPvXSSHfU4Qoy"},
{"username":"Fossil-26","wallet":"2EcTsncN6Evwdw7kA1dM6fGXrQXSQXzBDb7cAEW9N4X8"},
{"username":"Fossil-27","wallet":"AZm1yCMGdy792bqvKScZKRvaY8Br51TtFc7nFAHpUGe8"},
{"username":"Fossil-28","wallet":"2FRPmgqpFhXK4sNbD98N7yNN59ajhUQfHP8jagsatmEw"},
{"username":"Fossil-29","wallet":"GTgkUBxQuCuSBLzKfxUnqGVSo6LMo6d3icbhe6TECjQV"},
{"username":"Fossil-30","wallet":"GnuZSi5HdZauoxscyLVVeDnHx7XNjBKpcNJXYJutfZMJ"},
{"username":"Fossil-31","wallet":"9dYoDwHhb8Q1fmjqxBLkCcxFnbdy1xAhBohYQakuGctm"},
{"username":"Fossil-32","wallet":"EC1thPYmapQB2JeEVxDyuh6rSZjKxCas5JPnF7kVMA3J"},
{"username":"Fossil-33","wallet":"9bKdU86vQt9yPTV1eMtYo5SNL3X2S7FzpYaojeJ85wwm"},
{"username":"Fossil-34","wallet":"DZJzNYkZX12bNhyh6GAxrN4KyHANBhQdGjWvELC5VVNb"},
{"username":"Fossil-35","wallet":"1xgSwmiVjuhVrHktJQqp28zn9GRK8EAxukyotxk5pqj"},
{"username":"Fossil-36","wallet":"8hR75cBkNUA7jgcGkD3AdfBYyqjS8s3TZM5YDjHdKkZM"},
{"username":"Fossil-37","wallet":"HZxomh9GJNb2WTCn8t4jhkk39vrHdHFJLg8tEKWcTJyY"},
{"username":"Fossil-38","wallet":"CRZ7DbKMv4AKm2jmRYfPx7gbPa3BhTbpgqErm6rmtnvN"},
{"username":"Fossil-39","wallet":"5fG813NEEcdVre3NnDVCN3prL7T15YvxL6Tk5ob5f6Nn"},
{"username":"Fossil-40","wallet":"BxUtdniDSA1613th7xaBrxuuGDMuLvP2TpH2ykzEcvPX"},
{"username":"Fossil-41","wallet":"Ha9hFXmQnVSnDY2BAYozQzHcRGoLmM3wTERGr7zdWf3b"},
{"username":"Fossil-42","wallet":"8w2mwXwpQK3bYqDLqfvngpSei3wfkceQbFeMEWJY1y1n"},
{"username":"Fossil-43","wallet":"BRnjBVHBVMGuRcFaU6Em6ZrWJSzyUptW3dcAR4rwnDUC"},
{"username":"Fossil-44","wallet":"6FNELvZfSXTescZMR1geuw6o6cCvEPRLgymSPeCdWdR7"},
{"username":"Fossil-45","wallet":"FHGPeUW1VgF4SRwiZbGKa4Kqk2i39ogkrX4N6c5CNJec"},
{"username":"Fossil-46","wallet":"6peMxWonczQYTiFv7oT2zqsMKeaHevyoEFMRmf9VwyfG"},
{"username":"Fossil-47","wallet":"43CGozxcUW2jU87SX9KDhJjcDGwmBRno66tMUeaEhQqQ"},
{"username":"Fossil-48","wallet":"C257DgxqBfDNuPiTcJiAYGcFQiYFFpgXxLft9oDXdn3n"},
{"username":"Fossil-49","wallet":"EtxzvaU41NRJN8rKZvKuSPGMX94P7aWuPor4M8qunGHu"},
{"username":"Fossil-50","wallet":"6W2iDGhGqsn4UGKy4zgcqyqCpmf8Q3zRGNHjvhqKDSAX"},
{"username":"Fossil-51","wallet":"9F1NiRjo4QEiSzdL2JpPUT9KnyPP8nS6HdFLwLnAfedH"},
{"username":"Fossil-52","wallet":"DTtJBTFcRH6EiArKsHidD1jngJq6uYvRf8JngWhb9fwt"},
{"username":"Fossil-53","wallet":"DPigrEcZpBmjXdEcj4JeR8qbcRetJqZEhmZrHUuAZDmW"},
{"username":"Fossil-54","wallet":"9SdoEC5VYN883dhFb6L3j7tfoBb8Rtf9X8dPWUxcUGLk"},
{"username":"Fossil-55","wallet":"Dew1xPKDzMZ5TCc6gdDRsjiM2YfLainbMgnPXUGvJqRB"},
{"username":"Fossil-56","wallet":"7RkecPja61ebEgxZs5tovd7AqYtMb89vcEHm1zX3QoGf"},
{"username":"Fossil-57","wallet":"3kL8Ad4qYGascn54hHPAjmVwsrWUXtNQbeDarow3apVq"},
{"username":"Fossil-58","wallet":"CxB7M3afXaESzbrQJZhyEtvcqvRU9E6MuxZHS41T5pET"},
{"username":"Fossil-59","wallet":"DAAKm3Deok3jLgmB2rVmABDz7LHrZYqY15uVi19RLjYu"},
{"username":"Fossil-60","wallet":"BGYesmDxnzTV9QQdcxRqVWCHHxjQSvzJTa9tPafH8Udo"},
{"username":"Fossil-61","wallet":"3KBZe4E86d87NhYRWiZmgCdu2Wd3hbAN9sh4aeE3pJGP"},
{"username":"Fossil-62","wallet":"5Dbe9SLraPxR7LQXAmBEDs4fVErqoti7BKSfxaxZM3CA"},
{"username":"Fossil-63","wallet":"HodLtjDsNnd69Z7LRXMYeKD2mcEM5E8VGWiFHSC1Eiau"},
{"username":"Fossil-64","wallet":"7KoZPmLh5m8GVDabZTTw2yeyyzqrBq86b4wg1jLMdeAv"},
{"username":"Fossil-65","wallet":"HpfPxtik4HndokQDpdTH5jDoTq7nmfwjwhHoAtxNrxvS"},
{"username":"Fossil-66","wallet":"2EUS8niS5aNGgFu5MhXLsmaXWLj7dY51GHE3ocYNw893"},
{"username":"Fossil-67","wallet":"AqwXMfJCeqN111s6FZSjr5gkRWbBsBmtNpYhu5NJooaB"},
{"username":"Fossil-68","wallet":"51rvMzFNi1DnbhUp2u4MHEoU8wic6pWEnbLGBV3YqReJ"},
{"username":"Fossil-69","wallet":"G6xxLBTwT8toDdu9XngK6Qe4a53kfpUCFJxuUX23pfs8"},
{"username":"Fossil-70","wallet":"9hHEeY1sEW3YwZjLXPWDCVZaL8fHhqs4pDQzQQqmMBrK"},
{"username":"Fossil-71","wallet":"AxBQqULBVX1Upvrf1atMrVGajDgkBHoo34AqqQcja1HR"},
{"username":"Fossil-72","wallet":"9RywEj7ZMsi8LhTUYfo6rza2BUK38yb1LcyFfwJNM2u2"},
{"username":"Fossil-73","wallet":"5QPWQYx9qRjJ7RfXdriVPRcGdjnDoZYMQ2XjE11a1kue"},
{"username":"Fossil-74","wallet":"99NzQHbWT44YttBuUmoVEYapwyGxUHFn62w2EvaDcoqp"},
{"username":"Fossil-75","wallet":"9DFUPVW7WLqdXx4wcAMdsZhn11DCiuQbTGN24y9CJDW1"},
{"username":"Fossil-76","wallet":"4wTQovTfpVDhkJrSu1i4ZTbjYoRxUjKV2BsoeyMKQZNS"},
{"username":"Fossil-77","wallet":"7aoAfxnWLCZ78CsJeEb7XJduTtWnXHNZbsVJFYHBSBHM"},
{"username":"Fossil-78","wallet":"EXbtwCMScBbLXjx7XukMdb7vbMyE2CoZgP2mLRrExN1M"},
{"username":"Fossil-79","wallet":"6Tvz4fS28CkPsE1ZTe8voJr77JGt5bKepTENEpt6rVYf"},
{"username":"Fossil-80","wallet":"5Qbxe6SzcobJq7njouuSYask5Y1DjHLtZfLGG4mfMAJ1"},
{"username":"Fossil-81","wallet":"6Hvg1trypLen5836q1YpidbAs33d8JoncsTBdZkXjtH5"},
{"username":"Fossil-82","wallet":"37tuCxqrzKPyaKY7TDZ4Pvd9wBXxkrEDVRvTpPfiiUHd"},
{"username":"Fossil-83","wallet":"BmaJKLt6TRbhKcp6322SfKQV61HiyCQdkjvzLUTHfhvL"},
{"username":"Fossil-84","wallet":"9UT52uZ5ggjRcRaJfSGiu9QBb4ionCmpunRspy7bpTe7"},
{"username":"Fossil-85","wallet":"Ex58HJam4ggEqbC3z4aCK1vPwygk6KJbyXsekyXwT4mG"},
{"username":"Fossil-86","wallet":"EnJGEFkktHGqhXgTDSGs3CChWFA8hFXCxXAAcXp68Reo"},
{"username":"Fossil-87","wallet":"CNAzvkSGuomxNLXE3VWCSJzVqPq1XcUjx5NMuD5Q9QsV"},
{"username":"Fossil-88","wallet":"GKpMCbyKXVz9swgxwT8u93C5KfR9aZoomHXL4cecbuFW"},
{"username":"Fossil-89","wallet":"HmfpbQvNgEeS1VtNQWG7RuVe3cNp1bUZgSqfhJEQRTRy"},
{"username":"Fossil-90","wallet":"4spmqDTbc6tmrJZAbyru3WRprMX12qhW8xHwCEbevxQ8"},
{"username":"Fossil-91","wallet":"GZkdMM1VveNGLWTnHmfXszNk2PqU68K5JWDVXgCP7a4E"},
{"username":"Fossil-92","wallet":"FTvy5mJZthzutkdogcBkvrHpZXKcSQdrv53piTjSQ2Pi"},
{"username":"Fossil-93","wallet":"AoT35xVYXfRi3LqBcQ8m6uNgv2NUp5THXicyQ2NSKmHT"},
{"username":"Fossil-94","wallet":"7XZvgYh6Q1mJ5vk7CEATNScFvYruBZc9bf75rMsSCcjX"},
{"username":"Fossil-95","wallet":"DXRv6uUogZ1bXtGCvRtjJZKUsGsXAQ7SVet4UhaaAE9i"},
{"username":"Fossil-96","wallet":"E9Ngnn4mC6ZuU6GJ4A6sohFtNmUrrVRLcKGWy5BpUAEV"},
{"username":"Fossil-97","wallet":"Da6Y46KQ3ky5KjMUnfRAPqqWJzBio8wgkgdFxWCz29pz"},
{"username":"Fossil-98","wallet":"AhTaUmWJHwfdep8JPtkZAuizc6ELxXseG5Hx1gyAgR5P"},
{"username":"Fossil-99","wallet":"BZJqFt6mWgDM5w6HGkQTV497YWaXiRy55Ca7cYAgD1NC"},









    
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
  
