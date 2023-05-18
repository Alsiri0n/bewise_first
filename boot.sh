#!/bin/bash
exec uvicorn app.main:Application --reload --host 0.0.0.0