from ddgs import DDGS

from app.utils.logger import logger


class SearchTool:

    def search(
        self,
        query: str,
        max_results: int = 5
    ) -> dict:

        logger.info(
            f"Searching DuckDuckGo: {query}"
        )

        try:

            with DDGS() as ddgs:

                results = list(
                    ddgs.text(
                        query,
                        max_results=max_results
                    )
                )

            logger.info(
                f"Raw search results: {len(results)}"
            )

            processed_results = []

            for result in results:

                processed_results.append(
                    {
                        "title": result.get(
                            "title",
                            ""
                        ),
                        "body": result.get(
                            "body",
                            ""
                        ),
                        "href": result.get(
                            "href",
                            ""
                        )
                    }
                )

            logger.info(
                f"Processed results: {len(processed_results)}"
            )

            formatted_results = []

            for item in processed_results:

                formatted_results.append(
                    f"""
Title: {item['title']}

Content: {item['body']}

URL: {item['href']}
"""
                )

            search_results = "\n\n".join(
                formatted_results
            )

            logger.info(
                f"Search context length: {len(search_results)}"
            )

            return {
                "result_count": len(
                    processed_results
                ),
                "search_results": search_results
            }

        except Exception as ex:

            logger.exception(
                f"Search failed: {str(ex)}"
            )

            return {
                "result_count": 0,
                "search_results": ""
            }


search_tool = SearchTool()