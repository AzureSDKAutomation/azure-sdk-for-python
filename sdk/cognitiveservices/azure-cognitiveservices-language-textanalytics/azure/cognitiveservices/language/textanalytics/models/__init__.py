# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import AnalyzeBatchInput
    from ._models_py3 import AnalyzeJobMetadata
    from ._models_py3 import AnalyzeJobState
    from ._models_py3 import AnalyzeJobStateTasks
    from ._models_py3 import AnalyzeJobStateTasksDetails
    from ._models_py3 import AnalyzeJobStateTasksEntityRecognitionPiiTasksItem
    from ._models_py3 import AnalyzeJobStateTasksEntityRecognitionTasksItem
    from ._models_py3 import AnalyzeJobStateTasksKeyPhraseExtractionTasksItem
    from ._models_py3 import AspectConfidenceScoreLabel
    from ._models_py3 import AspectRelation
    from ._models_py3 import DetectedLanguage
    from ._models_py3 import DocumentEntities
    from ._models_py3 import DocumentError
    from ._models_py3 import DocumentHealthcareEntities
    from ._models_py3 import DocumentKeyPhrases
    from ._models_py3 import DocumentLanguage
    from ._models_py3 import DocumentLinkedEntities
    from ._models_py3 import DocumentSentiment
    from ._models_py3 import DocumentStatistics
    from ._models_py3 import EntitiesResult
    from ._models_py3 import EntitiesTask
    from ._models_py3 import EntitiesTaskParameters
    from ._models_py3 import Entity
    from ._models_py3 import EntityLinkingResult
    from ._models_py3 import ErrorResponse
    from ._models_py3 import HealthcareEntity
    from ._models_py3 import HealthcareEntityLink
    from ._models_py3 import HealthcareJobState
    from ._models_py3 import HealthcareRelation
    from ._models_py3 import HealthcareResult
    from ._models_py3 import InnerError
    from ._models_py3 import JobDescriptor
    from ._models_py3 import JobManifest
    from ._models_py3 import JobManifestTasks
    from ._models_py3 import JobMetadata
    from ._models_py3 import KeyPhraseResult
    from ._models_py3 import KeyPhrasesTask
    from ._models_py3 import KeyPhrasesTaskParameters
    from ._models_py3 import LanguageBatchInput
    from ._models_py3 import LanguageInput
    from ._models_py3 import LanguageResult
    from ._models_py3 import LinkedEntity
    from ._models_py3 import Match
    from ._models_py3 import MultiLanguageBatchInput
    from ._models_py3 import MultiLanguageInput
    from ._models_py3 import Pagination
    from ._models_py3 import PiiDocumentEntities
    from ._models_py3 import PiiResult
    from ._models_py3 import PiiTask
    from ._models_py3 import PiiTaskParameters
    from ._models_py3 import RequestStatistics
    from ._models_py3 import SentenceAspect
    from ._models_py3 import SentenceOpinion
    from ._models_py3 import SentenceSentiment
    from ._models_py3 import SentimentConfidenceScorePerLabel
    from ._models_py3 import SentimentResponse
    from ._models_py3 import TasksState
    from ._models_py3 import TaskState
    from ._models_py3 import TextAnalyticsError
    from ._models_py3 import TextAnalyticsWarning
except (SyntaxError, ImportError):
    from ._models import AnalyzeBatchInput
    from ._models import AnalyzeJobMetadata
    from ._models import AnalyzeJobState
    from ._models import AnalyzeJobStateTasks
    from ._models import AnalyzeJobStateTasksDetails
    from ._models import AnalyzeJobStateTasksEntityRecognitionPiiTasksItem
    from ._models import AnalyzeJobStateTasksEntityRecognitionTasksItem
    from ._models import AnalyzeJobStateTasksKeyPhraseExtractionTasksItem
    from ._models import AspectConfidenceScoreLabel
    from ._models import AspectRelation
    from ._models import DetectedLanguage
    from ._models import DocumentEntities
    from ._models import DocumentError
    from ._models import DocumentHealthcareEntities
    from ._models import DocumentKeyPhrases
    from ._models import DocumentLanguage
    from ._models import DocumentLinkedEntities
    from ._models import DocumentSentiment
    from ._models import DocumentStatistics
    from ._models import EntitiesResult
    from ._models import EntitiesTask
    from ._models import EntitiesTaskParameters
    from ._models import Entity
    from ._models import EntityLinkingResult
    from ._models import ErrorResponse
    from ._models import HealthcareEntity
    from ._models import HealthcareEntityLink
    from ._models import HealthcareJobState
    from ._models import HealthcareRelation
    from ._models import HealthcareResult
    from ._models import InnerError
    from ._models import JobDescriptor
    from ._models import JobManifest
    from ._models import JobManifestTasks
    from ._models import JobMetadata
    from ._models import KeyPhraseResult
    from ._models import KeyPhrasesTask
    from ._models import KeyPhrasesTaskParameters
    from ._models import LanguageBatchInput
    from ._models import LanguageInput
    from ._models import LanguageResult
    from ._models import LinkedEntity
    from ._models import Match
    from ._models import MultiLanguageBatchInput
    from ._models import MultiLanguageInput
    from ._models import Pagination
    from ._models import PiiDocumentEntities
    from ._models import PiiResult
    from ._models import PiiTask
    from ._models import PiiTaskParameters
    from ._models import RequestStatistics
    from ._models import SentenceAspect
    from ._models import SentenceOpinion
    from ._models import SentenceSentiment
    from ._models import SentimentConfidenceScorePerLabel
    from ._models import SentimentResponse
    from ._models import TasksState
    from ._models import TaskState
    from ._models import TextAnalyticsError
    from ._models import TextAnalyticsWarning
from ._text_analytics_client_enums import (
    AspectRelationType,
    DocumentSentimentValue,
    ErrorCodeValue,
    InnerErrorCodeValue,
    SentenceSentimentValue,
    State,
    StringIndexType,
    StringIndexTypeResponse,
    TokenSentimentValue,
    WarningCodeValue,
)

__all__ = [
    'AnalyzeBatchInput',
    'AnalyzeJobMetadata',
    'AnalyzeJobState',
    'AnalyzeJobStateTasks',
    'AnalyzeJobStateTasksDetails',
    'AnalyzeJobStateTasksEntityRecognitionPiiTasksItem',
    'AnalyzeJobStateTasksEntityRecognitionTasksItem',
    'AnalyzeJobStateTasksKeyPhraseExtractionTasksItem',
    'AspectConfidenceScoreLabel',
    'AspectRelation',
    'DetectedLanguage',
    'DocumentEntities',
    'DocumentError',
    'DocumentHealthcareEntities',
    'DocumentKeyPhrases',
    'DocumentLanguage',
    'DocumentLinkedEntities',
    'DocumentSentiment',
    'DocumentStatistics',
    'EntitiesResult',
    'EntitiesTask',
    'EntitiesTaskParameters',
    'Entity',
    'EntityLinkingResult',
    'ErrorResponse',
    'HealthcareEntity',
    'HealthcareEntityLink',
    'HealthcareJobState',
    'HealthcareRelation',
    'HealthcareResult',
    'InnerError',
    'JobDescriptor',
    'JobManifest',
    'JobManifestTasks',
    'JobMetadata',
    'KeyPhraseResult',
    'KeyPhrasesTask',
    'KeyPhrasesTaskParameters',
    'LanguageBatchInput',
    'LanguageInput',
    'LanguageResult',
    'LinkedEntity',
    'Match',
    'MultiLanguageBatchInput',
    'MultiLanguageInput',
    'Pagination',
    'PiiDocumentEntities',
    'PiiResult',
    'PiiTask',
    'PiiTaskParameters',
    'RequestStatistics',
    'SentenceAspect',
    'SentenceOpinion',
    'SentenceSentiment',
    'SentimentConfidenceScorePerLabel',
    'SentimentResponse',
    'TasksState',
    'TaskState',
    'TextAnalyticsError',
    'TextAnalyticsWarning',
    'StringIndexTypeResponse',
    'ErrorCodeValue',
    'InnerErrorCodeValue',
    'WarningCodeValue',
    'DocumentSentimentValue',
    'SentenceSentimentValue',
    'TokenSentimentValue',
    'AspectRelationType',
    'State',
    'StringIndexType',
]
