from datetime import datetime
from typing import Dict, Generator,  Protocol


class IApiYoutube(Protocol):

    def checar_conexao(self) -> bool:
        ...

    def obter_video_por_data(
            self,
            data_inicio: datetime
    ) -> Generator[Dict, None, None]:
        ...
