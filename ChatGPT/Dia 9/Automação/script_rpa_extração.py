from rpa import Browser

# Crie uma instância do navegador
browser = Browser()

# Abra uma página da web
browser.open_available_browser("https://www.exemplo.com")

# Execute ações no site, como preencher formulários, clicar em botões, etc.
browser.input_text("id:nome", "Exemplo")
browser.input_text("id:email", "exemplo@exemplo.com")
browser.click_button("id:enviar")

# Extraia os dados que você precisa do site
nome = browser.get_text("id:nome")
email = browser.get_text("id:email")

# Feche o navegador
browser.close_browser()
