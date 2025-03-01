import banco

ze = banco.Banco("Saqua Eng Software", 1, 1, "Zé da Manga", "12345678900")

zecove = banco.Banco("Inter", 1, 1006, "Zé das Coves", "00987465123")

joao = banco.Banco("Imaginario", 1, 1, "João", "00123456789")

print(ze)

print(zecove)

zecove.definir_senha(12345)
ze.definir_senha("admin01")

ze.deposito(5000)

zecove.extrato()

ze.pix(zecove, 2000)

ze.pix(joao, 1000)

ze.saque("admin01", 1000)

zecove.pix(ze, 1000)

ze.extrato()

zecove.extrato()

joao.extrato()

ze.caixinha_invest(500, 2)

ze.calcular_rendimento()

ze.extrato()