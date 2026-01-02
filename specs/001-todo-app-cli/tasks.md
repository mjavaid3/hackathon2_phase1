---

description: "Task list template for feature implementation"
---

# Tasks: Todo App CLI

**Input**: Design documents from `/specs/[###-feature-name]/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Constitution Compliance**: All tasks must adhere to the project constitution principles

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

<!--
  ============================================================================
  IMPORTANT: The tasks below are SAMPLE TASKS for illustration purposes only.

  The /sp.tasks command MUST replace these with actual tasks based on:
  - User stories from spec.md (with their priorities P1, P2, P3...)
  - Feature requirements from plan.md
  - Entities from data-model.md
  - Endpoints from contracts/

  Tasks MUST be organized by user story so each story can be:
  - Implemented independently
  - Tested independently
  - Delivered as an MVP increment

  DO NOT keep these sample tasks in the generated tasks.md file.
  ============================================================================
-->

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project structure per implementation plan: src/todo_app/__init__.py, src/todo_app/main.py, src/todo_app/models.py, src/todo_app/storage.py, src/todo_app/cli.py
- [ ] T002 Initialize Python 3.12+ project with UV dependency management (Constitution: Technology & Constraints)
- [ ] T003 [P] Configure linting and formatting tools (Constitution: Code Quality & Structure Requirements)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T004 Setup in-memory storage structure (Constitution: Additional Functional Requirements - tasks stored in memory only)
- [X] T005 [P] Implement CLI interface framework (Constitution: Additional Functional Requirements - interactive command loop)
- [X] T006 [P] Setup command parsing and handling (Constitution: Additional Functional Requirements - help, exit/quit commands)
- [X] T007 Create Task model/dataclass (Constitution: Required Features Implementation - Add Task feature)
- [X] T008 Configure error handling and validation (Constitution: Additional Functional Requirements - input validation)
- [ ] T009 Setup project documentation structure (Constitution: Deliverables - README.md, QWEN.md)

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add New Tasks (Priority: P1) 🎯 MVP

**Goal**: Enable users to add new tasks to their list so they can keep track of things they need to do.

**Independent Test**: Can be fully tested by adding a task with a title and description and verifying it appears in the task list with a unique ID and "incomplete" status.

### Implementation for User Story 1

- [X] T010 [P] [US1] Create Task model in src/todo_app/models.py with dataclass definition and type hints
- [X] T011 [P] [US1] Create InMemoryStorage class in src/todo_app/storage.py with add_task method
- [X] T012 [US1] Implement add command handler in src/todo_app/cli.py
- [X] T013 [US1] Integrate add command with storage layer
- [X] T014 [US1] Add validation for required title field
- [X] T015 [US1] Add error handling for empty titles

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View All Tasks (Priority: P1)

**Goal**: Enable users to view all their tasks so they can see what they need to do.

**Independent Test**: Can be fully tested by adding a few tasks and then using the list command to view them all in a clear, readable format.

### Implementation for User Story 2

- [X] T016 [P] [US2] Enhance InMemoryStorage class with list_tasks method in src/todo_app/storage.py
- [X] T017 [US2] Implement list command handler in src/todo_app/cli.py
- [X] T018 [US2] Format task display with ID, Title, Description, and Status
- [X] T019 [US2] Handle case when no tasks exist

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 6 - Interactive Command Interface (Priority: P1)

**Goal**: Enable users to interact with the application through a command prompt so that they can efficiently manage their tasks.

**Independent Test**: Can be fully tested by entering various commands and receiving appropriate responses from the application.

### Implementation for User Story 6

- [X] T020 [P] [US6] Implement main REPL loop in src/todo_app/main.py
- [X] T021 [US6] Create command dispatcher dictionary in src/todo_app/cli.py
- [X] T022 [US6] Implement help command handler
- [X] T023 [US6] Implement exit/quit command handlers
- [X] T024 [US6] Add command prompt display ("> ")

**Checkpoint**: At this point, User Stories 1, 2 AND 6 should all work independently

---

## Phase 6: User Story 3 - Update Task Details (Priority: P2)

**Goal**: Enable users to update their tasks so that they can modify titles or descriptions as needed.

**Independent Test**: Can be fully tested by updating a task's title or description and verifying the changes are reflected when viewing the task list.

### Implementation for User Story 3

- [X] T025 [P] [US3] Enhance InMemoryStorage class with update_task method in src/todo_app/storage.py
- [X] T026 [US3] Implement update command handler in src/todo_app/cli.py
- [X] T027 [US3] Add validation for task ID existence
- [X] T028 [US3] Handle partial updates (title or description only)

**Checkpoint**: At this point, User Stories 1, 2, 3 AND 6 should all work independently

---

## Phase 7: User Story 4 - Delete Tasks (Priority: P2)

**Goal**: Enable users to delete tasks that they no longer need so that they can keep their list organized.

**Independent Test**: Can be fully tested by deleting a task and verifying it no longer appears when viewing the task list.

### Implementation for User Story 4

- [X] T029 [P] [US4] Enhance InMemoryStorage class with delete_task method in src/todo_app/storage.py
- [X] T030 [US4] Implement delete command handler in src/todo_app/cli.py
- [X] T031 [US4] Add validation for task ID existence

**Checkpoint**: At this point, User Stories 1, 2, 3, 4 AND 6 should all work independently

---

## Phase 8: User Story 5 - Mark Tasks Complete/Incomplete (Priority: P2)

**Goal**: Enable users to mark tasks as complete or incomplete so that they can track their progress.

**Independent Test**: Can be fully tested by marking a task as complete and verifying the status changes when viewing the task list.

### Implementation for User Story 5

- [X] T032 [P] [US5] Enhance InMemoryStorage class with complete_task and incomplete_task methods in src/todo_app/storage.py
- [X] T033 [US5] Implement complete command handler in src/todo_app/cli.py
- [X] T034 [US5] Implement incomplete command handler in src/todo_app/cli.py
- [X] T035 [US5] Add validation for task ID existence

**Checkpoint**: All user stories should now be independently functional

---

## Phase 9: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T036 [P] Documentation updates in README.md (Constitution: Deliverables - README.md with setup/run instructions)
- [X] T037 Code cleanup and refactoring (Constitution: Code Quality & Structure Requirements)
- [X] T038 [P] Input validation improvements across all commands
- [X] T039 Error message consistency improvements
- [X] T040 Run quickstart.md validation (Constitution: Deliverables - fully working console app)

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Phase 9)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 6 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 4 (P2)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 5 (P2)**: Can start after Foundational (Phase 2) - No dependencies on other stories

### Within Each User Story

- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all models for User Story 1 together:
Task: "Create Task model in src/todo_app/models.py with dataclass definition and type hints"
Task: "Create InMemoryStorage class in src/todo_app/storage.py with add_task method"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 6 → Test independently → Deploy/Demo
5. Add User Story 3 → Test independently → Deploy/Demo
6. Add User Story 4 → Test independently → Deploy/Demo
7. Add User Story 5 → Test independently → Deploy/Demo
8. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 6
   - Developer D: User Story 3
   - Developer E: User Story 4
   - Developer F: User Story 5
3. Stories complete and integrate independently

---

## Constitution Compliance Notes

- All code must be generated by Qwen (No Manual Coding Allowed)
- Follow strict PEP 8 guidelines and include type hints (Code Quality & Structure Requirements)
- Use only Python standard library (Technology & Constraints)
- Store tasks in memory only (Additional Functional Requirements)
- Implement all 5 required features (Required Features Implementation)
- Include proper error handling and validation (Additional Functional Requirements)
- Ensure all deliverables are included (Deliverables section)

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence