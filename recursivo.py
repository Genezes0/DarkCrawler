if __name__ == "__main__":
    while True:
        start_url = "http://tordexu73joywapk2txdr54jed4imqledpcvcuf75qsas2gwdgksvnyd.onion"
        search_term = input("Digite o termo de busca: ")
        max_depth = 3  # Profundidade máxima de rastreamento
        visited_urls = set()
        relevant_links = []

        def recursive_crawler(url, depth):
            if depth <= 0 or url in visited_urls:
                return

            visited_urls.add(url)
            page = search_page(url, search_term)
            if page:
                relevant_links.extend(extract_links(page, search_term))
                change_tor_ip()

            for link in relevant_links:
                recursive_crawler(link, depth - 1)

        recursive_crawler(start_url, max_depth)

        # Treinar o modelo de IA com os links relevantes encontrados
        X = relevant_links
        y = [1] * len(relevant_links)
        train_model(X, y)

        # Prever relevância de novos links
        new_links = ["http://example.com", "http://another-example.com"]
        predictions = predict_relevance(new_links)
        for link, prediction in zip(new_links, predictions):
            if prediction == 1:
                print(f"O link {link} é relevante.")
            else:
                print(f"O link {link} não é relevante.")

        another_search = input("Realizar outra busca? (sim ou não): ").lower()
        if another_search != 'sim':
            break
