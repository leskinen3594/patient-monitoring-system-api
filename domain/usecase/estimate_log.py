from datetime import datetime
from typing import List, Tuple

from domain.entities import EstimateLog
from domain.registry import Registry


async def create_new_log(logReq: List[str], createdAt: datetime) -> Tuple[str]:
    repo = Registry().log_repository
    log_id: str = await repo.generate_log_id()
    estimate_log = EstimateLog.create_new_log_with_items(id=log_id, logList=logReq, createDate=createdAt)
    message = await repo.insert(estimate_log)
    return (log_id, message)


async def get_all_log() -> EstimateLog:
    repo = Registry().log_repository
    estimate_logs = await repo.select_all()
    return estimate_logs


async def get_one_log(logId: str) -> EstimateLog:
    repo = Registry().log_repository
    estimate_log = await repo.select_by_id(logId)
    return estimate_log


async def update_log_info(log: EstimateLog, logReq: List[str], updatedAt: datetime) -> str:
    repo = Registry().log_repository
    log_update = EstimateLog.update_log_with_id(logList=logReq, updateDate=updatedAt)
    message = await repo.update(log, log_update)
    return message


async def delete_log(log: EstimateLog):
    repo = Registry().log_repository
    message = await repo.delete(log)
    return message