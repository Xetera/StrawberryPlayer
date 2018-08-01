import pytest
from test.test_app import ytdl_client
import datetime
from youtube import download


@pytest.mark.asyncio
async def test_fetch_info():
    start = datetime.datetime.now()
    response = await download.fetch_info(ytdl_client, 'slipknot custer', 'test-client')
    end: datetime.timedelta = datetime.datetime.now() - start
    assert end.seconds < 5
    assert isinstance(response, dict)
    assert response['entries'][0]['uploader'] == 'Slipknot'

