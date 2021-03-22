from dataclasses import dataclass


@dataclass()
class PullRequest:
    id: int
    title: str
    creation_date: str
    state: str


@dataclass()
class Fork:
    id: int
    owner: str
    creation_date: str


@dataclass()
class Issue:
    id: int
    title: str
    description: str
    creation_date: str
