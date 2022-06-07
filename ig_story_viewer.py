from playwright.async_api import async_playwright
import asyncio
import pyautogui as p
import time


# define a function to login to instagram using username and password
async def login(page):
    # Click text=Consenti solo i cookie essenziali
    await page.locator("text=Consenti solo i cookie essenziali").click()
    # Click [aria-label="Numero\ di\ telefono\,\ nome\ utente\ o\ e-mail"]
    await page.locator("[aria-label=\"Numero\\ di\\ telefono\\,\\ nome\\ utente\\ o\\ e-mail\"]").click()
    # Fill [aria-label="Numero\ di\ telefono\,\ nome\ utente\ o\ e-mail"]
    await page.locator("[aria-label=\"Numero\\ di\\ telefono\\,\\ nome\\ utente\\ o\\ e-mail\"]").fill("gios.traio")
    # Click [aria-label="Password"]
    await page.locator("[aria-label=\"Password\"]").click()
    # Fill [aria-label="Password"]
    await page.locator("[aria-label=\"Password\"]").fill("Ghay6tu")
    # Click button:has-text("Accedi") >> nth=0
    await page.locator("button:has-text(\"Accedi\")").first.click()
    # Click text=Non ora
    await page.locator("text=Non ora").click()
    # assert page.url == "https://www.instagram.com/"
    # Click text=Non ora
    await page.locator("text=Non ora").click()


async def click_first_story(page):
    time.sleep(1.5)
    p.click(235, 222)
    await page.locator("[aria-label=\"Avanti\"]").nth(-1).click()


async def click_n_stories(page, n):
    urls = []
    import time
    for i in range(n):
        time.sleep(2.5)
        await page.locator("[aria-label=\"Avanti\"]").click()
        url = page.url.split("/")[-3]
        # make a tuple of the url and the time it was saved at
        urls.append((url, time.time()))

    # save each url to a file in the current directory
    with open("urls.txt", "a") as f:
        for url, timestamp in urls:
            f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} -> {url}\n")



# start a browser instance and a page context with a context manager
async def main():
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=False, slow_mo=150)
        page = await browser.new_page()
        # go to the instagram login page
        await page.goto("https://instagram.com/accounts/login/")
        await login(page)
        await click_first_story(page)
        await click_n_stories(page, 300)

        await page.pause()


if __name__ == '__main__':
    asyncio.run(main())
