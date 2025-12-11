#!/usr/bin/env python3
import click
import requests

BASE = "https://hefftools.dev/api/v1"

@click.group()
def cli():
    """HeffTools Command-line Utilities"""
    pass

@cli.command()
@click.option("--count", default=1, help="Number of UUIDs to generate")
def uuid(count):
    """Generate UUIDs"""
    r = requests.get(f"{BASE}/uuid/generate", params={"count": count})
    click.echo(r.text)

@cli.command()
@click.option("--length", default=16)
@click.option("--charset", default="strong")
def password(length, charset):
    """Generate passwords"""
    r = requests.get(f"{BASE}/password/generate",
                     params={"length": length, "charset": charset})
    click.echo(r.text)

@cli.command()
@click.argument("text")
def urlencode(text):
    """URL encode text"""
    r = requests.post(f"{BASE}/url/encode", json={"text": text})
    click.echo(r.text)

@cli.command()
@click.argument("text")
def urldecode(text):
    """URL decode text"""
    r = requests.post(f"{BASE}/url/decode", json={"text": text})
    click.echo(r.text)

@cli.command()
@click.argument("cidr")
def subnet(cidr):
    """Calculate subnet info"""
    r = requests.post(f"{BASE}/subnet/calc", json={"cidr": cidr})
    click.echo(r.text)

if __name__ == "__main__":
    cli()

