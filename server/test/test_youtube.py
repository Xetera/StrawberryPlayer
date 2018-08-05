import pytest
from test.test_app import ytdl_client
import datetime
from youtube import download


@pytest.mark.asyncio
@pytest.mark.first
async def test_can_fetch_info():
    # Father forgive my sins for using the unspeakable keyword
    # but I can't call functions directly in these tests
    global response
    global end
    start = datetime.datetime.now()
    response = await download.fetch_info(ytdl_client, 'slipknot custer', 'test-client')
    end = datetime.datetime.now() - start
    assert isinstance(response, dict)


@pytest.mark.run(after='test_can_fetch_info')
def test_downloads_in_reasonable_time():
    assert end.seconds < 10


@pytest.mark.run(after='test_can_fetch_info')
def test_finds_top_result():
    assert response['entries'][0]['uploader'] == 'Slipknot'

