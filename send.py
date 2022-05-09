#!/usr/bin/env python
import pika
import os

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=os.environ.get("RABBITMQ_HOST"))
)
channel = connection.channel()

channel.queue_declare(queue="urls")


urls = [
    "minha-serie/238164-ordem-cronologica-filmes-series-marvel-confira.htm",
    "voxel/238069-minecraft-criar-servidor-game.htm",
    "mercado/238200-apple-nao-aceita-cartoes-credito-debito-india.htm",
    "internet/238197-mailtrack-usar-gmail.htm",
    "internet/238079-gmail-veja-cancelar-envio-mail.htm",
    "produto/238199-veja-orimeiros-cabos-usb-c-padrao-2-1-240w.htm",
    "mercado/237981-pesquisador-ia-demitido-desafiar-google.htm",
    "cultura-geek/238193-sam-raimi-doutor-estranho-2-nao-primeiro-filme-heroi-veja.htm",
    "voxel/236534-melhores-jogos-coop-jogar-amigos-pc.htm",
    "software/238198-whatsapp-usar-novas-reacoes-mensagens.htm",
    "internet/238197-mailtrack-usar-gmail.htm",
    "minha-serie/238196-doctor-who-ator-sex-education-novo-protagonista.htm",
]


for url in urls:
    print(f" [x] {url}")
    channel.basic_publish(exchange="", routing_key="urls", body=url)

print(" [x] Concluído envio de todas URLS")
connection.close()
