from random import randint, choice

# **Іпс - 12 Шовкопляс Богдан Вікторович **
# Генератор “відомих цитат”: запровадьте програму,
# яка генерує нову цитату за допомогою моделі ланцюга
# Маркова. Програма має використовувати масив для зберігання
# вхідних цитат і інший масив для зберігання моделі ланцюга Маркова.
# Програма повинна запитати у користувача довжину згенерованої цитати та
# порядок моделі ланцюга Маркова.

paragraph = "No doubt I now grew very pale; " \
            "--but I talked more fluently, and with a " \
            "heightened voice. Yet the sound increased " \
            "--and what could I do? It was a low, dull, " \
            "quick sound --much such a sound as a watch " \
            "makes when enveloped in cotton. I gasped for " \
            "breath -- and yet the officers heard it not. " \
            "I talked more quickly --more vehemently; but " \
            "the noise steadily increased. I arose and argued " \
            "about trifles, in a high key and with violent " \
            "gesticulations; but the noise steadily increased. " \
            "Why would they not be gone? I paced the floor to " \
            "and fro with heavy strides, as if excited to fury " \
            "by the observations of the men -- but the noise steadily " \
            "increased. Oh God! what could I do? I foamed --I raved --I " \
            "swore! I swung the chair upon which I had been sitting, and " \
            "grated it upon the boards, but the noise arose over all and " \
            "continually increased. It grew louder --louder --louder! " \
            "And still the men chatted pleasantly, and smiled. Was it " \
            "possible they heard not? Almighty God! --no, no! They heard! " \
            "--they suspected! --they knew! --they were making a mockery of " \
            "my horror! --this I thought, and this I think. But anything was " \
            "better than this agony! Anything was more tolerable than this derision! " \
            "I could bear those hypocritical smiles no longer! I felt that I must " \
            "scream or die! --and now --again! --hark! louder! louder! louder! louder!"


def remove_signs(el: str):
    el = el.replace("!", "")
    el = el.replace(".", "")
    el = el.replace(",", "")
    el = el.replace("?", "")
    return el


def first_filter(el: str):
    return "--" in el


def generate_quote(length: int, firsts: list[str], elses: list[str]):
    if length <= 1:
        return "Length must be not less than 2"
    quote = str(choice(words)).title()
    for i in range(length):
        quote += " " + str(choice(elses)).lower()

    return quote


if __name__ == '__main__':
    words: list[str] = paragraph.split()
    words = list(map(remove_signs, words))

    firsts = list(map(lambda x: x.replace("--", ""), filter(first_filter, words)))
    else_words = list(filter(lambda x: not first_filter(x), words))

    quote_length = int(input("Quote length: "))

    print(generate_quote(quote_length, firsts, else_words))
