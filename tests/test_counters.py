from playwright.sync_api import Page, expect

def test_counter_CO2(page: Page):
    page.goto('https://www.avito.ru/avito-care/eco-impact?from=avito-care-navigation')
    
    counters = page.locator('.desktop-impact-item-eeQO3')
    counter_CO2 = counters.nth(1)
    expect(counter_CO2).to_be_visible()
    expect(counter_CO2).to_have_css("border-radius", "40px")
    expect(counter_CO2).to_have_css("height", "226px")
    expect(counter_CO2).to_have_css("width", "226px")


    counters_values = page.locator('.desktop-value-Nd1tR')
    counter_value_CO2 = counters_values.nth(0)
    expect(counter_value_CO2).to_be_visible()
    expect(counter_value_CO2).to_have_css("text-align", "center")
    expect(counter_value_CO2).to_have_css("color", "rgb(20, 20, 20)")
    expect(counter_value_CO2).to_have_css("font-size", "70.129px")
    expect(counter_value_CO2).to_have_css("font-family", "Manrope, arial, serif")

    unit_CO2 = page.locator('.desktop-unit-puWVS').get_by_text('кг CO₂')
    expect(unit_CO2).to_be_visible()
    expect(unit_CO2).to_have_css("font-size", "20.72px")
    expect(unit_CO2).to_have_css("color", "rgb(20, 20, 20)")
    expect(unit_CO2).to_have_css("text-align", "center")
    expect(unit_CO2).to_have_css("font-family", "Manrope, arial, serif")

    description_CO2 = page.locator('.desktop-label-EIkG9').get_by_text('не попало в атмосферу')
    expect(description_CO2).to_be_visible()
    expect(description_CO2).to_have_css("font-size", "13px")
    expect(description_CO2).to_have_css("text-align", "center")
    expect(description_CO2).to_have_css("color", "rgb(92, 92, 92)")
    expect(description_CO2).to_have_css("font-family", "Manrope, arial, serif")

    image_bird = page.locator('.desktop-bird-xXtiX')
    expect(image_bird).to_be_visible()
    expect(image_bird).to_have_css("position", "absolute")
    expect(image_bird).to_have_css("top", "-93px")
    expect(image_bird).to_have_css("left", "157px")
    expect(image_bird).to_have_css("width", "89px")
    expect(image_bird).to_have_css("height", "92px")


    counter_CO2.screenshot(path="output/test_counter_CO2.png")

def test_counter_water(page: Page):
    page.goto('https://www.avito.ru/avito-care/eco-impact?from=avito-care-navigation')

    counters = page.locator('.desktop-impact-item-eeQO3')
    counter_water = counters.nth(3)
    expect(counter_water).to_be_visible()
    expect(counter_water).to_have_css("border-radius", "40px")
    expect(counter_water).to_have_css("height", "226px")
    expect(counter_water).to_have_css("width", "226px")

    counters_values = page.locator('.desktop-value-Nd1tR')
    counter_value_water = counters_values.nth(1)
    expect(counter_value_water).to_be_visible()
    expect(counter_value_water).to_have_css("text-align", "center")
    expect(counter_value_water).to_have_css("color", "rgb(20, 20, 20)")
    expect(counter_value_water).to_have_css("font-size", "70.129px")
    expect(counter_value_water).to_have_css("font-family", "Manrope, arial, serif")

    unit_water = page.locator('.desktop-unit-puWVS').get_by_text('л воды')
    expect(unit_water).to_be_visible()
    expect(unit_water).to_have_css("font-size", "20.72px")
    expect(unit_water).to_have_css("color", "rgb(20, 20, 20)")
    expect(unit_water).to_have_css("text-align", "center")
    expect(unit_water).to_have_css("font-family", "Manrope, arial, serif")

    description_water = page.locator('.desktop-label-EIkG9').get_by_text('было сохранено')
    expect(description_water).to_be_visible()
    expect(description_water).to_have_css("font-size", "13px")
    expect(description_water).to_have_css("text-align", "center")
    expect(description_water).to_have_css("color", "rgb(92, 92, 92)")
    expect(description_water).to_have_css("font-family", "Manrope, arial, serif")

    image_water_1 = page.locator(".desktop-water1-LWlZZ")
    expect(image_water_1).to_be_visible()
    expect(image_water_1).to_have_css("position", "absolute")
    expect(image_water_1).to_have_css("top", "9px")
    expect(image_water_1).to_have_css("left", "172px")
    expect(image_water_1).to_have_css("width", "16px")
    expect(image_water_1).to_have_css("height", "33px")

    image_water_2 = page.locator(".desktop-water2-Fta24")
    expect(image_water_2).to_be_visible()
    expect(image_water_2).to_have_css("position", "absolute")
    expect(image_water_2).to_have_css("top", "42px")
    expect(image_water_2).to_have_css("left", "194px")
    expect(image_water_2).to_have_css("width", "19px")
    expect(image_water_2).to_have_css("height", "40px")

    counter_water.screenshot(path="output/test_counter_water.png")

def test_counter_energy(page: Page):
    page.goto('https://www.avito.ru/avito-care/eco-impact?from=avito-care-navigation')

    counters = page.locator('.desktop-impact-item-eeQO3')
    counter_energy = counters.nth(5)
    expect(counter_energy).to_be_visible()
    expect(counter_energy).to_have_css("border-radius", "40px")
    expect(counter_energy).to_have_css("height", "226px")
    expect(counter_energy).to_have_css("width", "226px")
    
    counters_values = page.locator('.desktop-value-Nd1tR')
    counter_value_energy = counters_values.nth(2)
    expect(counter_value_energy).to_be_visible()
    expect(counter_value_energy).to_have_css("text-align", "center")
    expect(counter_value_energy).to_have_css("color", "rgb(20, 20, 20)")
    expect(counter_value_energy).to_have_css("font-size", "70.129px")
    expect(counter_value_energy).to_have_css("font-family", "Manrope, arial, serif")

    unit_energy = page.locator('.desktop-unit-puWVS').get_by_text('кВт⋅ч энергии')
    expect(unit_energy).to_be_visible()
    expect(unit_energy).to_have_css("font-size", "20.72px")
    expect(unit_energy).to_have_css("color", "rgb(20, 20, 20)")
    expect(unit_energy).to_have_css("text-align", "center")
    expect(unit_energy).to_have_css("font-family", "Manrope, arial, serif")

    description_energy = page.locator('.desktop-label-EIkG9').get_by_text('было сэкономлено')
    expect(description_energy).to_be_visible()
    expect(description_energy).to_have_css("font-size", "13px")
    expect(description_energy).to_have_css("text-align", "center")
    expect(description_energy).to_have_css("color", "rgb(92, 92, 92)")
    expect(description_energy).to_have_css("font-family", "Manrope, arial, serif")

    image_sun = page.locator('.desktop-sun-JCEQH')
    expect(image_sun).to_be_visible()
    expect(image_sun).to_have_css("position", "absolute")
    expect(image_sun).to_have_css("top", "-19px")
    expect(image_sun).to_have_css("left", "169px")
    expect(image_sun).to_have_css("width", "83px")
    expect(image_sun).to_have_css("height", "89px")

    counter_energy.screenshot(path="output/test_counter_energy.png")
