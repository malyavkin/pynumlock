from queue import Queue

from icon import IconMgr
from common import icons
from state import State

Q = Queue()
stateMgr = State(Q)
mgr = IconMgr(Q, icons)
