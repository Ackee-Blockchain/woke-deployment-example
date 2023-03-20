from woke.deployment import *
from pytypes.contracts.Counter import Counter

NODE_URL = "ENTER_NODE_URL_HERE"


@default_chain.connect(NODE_URL)
def main():
    default_chain.set_default_accounts(Account.from_alias("deployment"))

    counter = Counter.deploy()
    print("Counter deployed at", counter.address)
