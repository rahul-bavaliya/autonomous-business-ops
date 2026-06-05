from fileinput import filename
import json
from pathlib import Path
import re
from app.utils.logger import logger


class FileTool:

    def save_json(
        self,
        filename: str,
        data: dict
    ):

        output_dir = Path("outputs")

        output_dir.mkdir(
            exist_ok=True
        )

        filepath = output_dir / filename

        with open(
            filepath,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                indent=4
            )

        logger.info(
            f"Saved report: {filepath}"
        )

file_tool = FileTool()