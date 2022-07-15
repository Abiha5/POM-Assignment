class homepagelocators():

    enter_textbo_xpath = "//input[@id='gh-ac']"
    click_catagories_xpath = "//select[@id='gh-cat']"
    click_select_item_xpath = "//select[@id='gh-cat']/option[@value='15032']"
    click_search_btn_xpath = "//input[@id='gh-btn']"

class searchpagelocators():

    search_results = "//h1[contains(text(), '+ results for')]"
    nth_item = "//div[@id='srp-river-results']/ul/li[7]"
    all_products = "/div[@id='srp-river-results']/ul/li"
