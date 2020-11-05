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

from msrest.serialization import Model
from msrest.exceptions import HttpOperationError


class ContextDTO(Model):
    """Context associated with Qna.

    :param is_context_only: To mark if a prompt is relevant only with a
     previous question or not.
     true - Do not include this QnA as search result for queries without
     context
     false - ignores context and includes this QnA in search result
    :type is_context_only: bool
    :param prompts: List of prompts associated with the answer.
    :type prompts:
     list[~azure.cognitiveservices.knowledge.qnamaker.runtime.models.PromptDTO]
    """

    _validation = {
        'prompts': {'max_items': 20},
    }

    _attribute_map = {
        'is_context_only': {'key': 'isContextOnly', 'type': 'bool'},
        'prompts': {'key': 'prompts', 'type': '[PromptDTO]'},
    }

    def __init__(self, *, is_context_only: bool=None, prompts=None, **kwargs) -> None:
        super(ContextDTO, self).__init__(**kwargs)
        self.is_context_only = is_context_only
        self.prompts = prompts


class Error(Model):
    """The error object. As per Microsoft One API guidelines -
    https://github.com/Microsoft/api-guidelines/blob/vNext/Guidelines.md#7102-error-condition-responses.

    All required parameters must be populated in order to send to Azure.

    :param code: Required. One of a server-defined set of error codes.
     Possible values include: 'BadArgument', 'Forbidden', 'NotFound',
     'KbNotFound', 'Unauthorized', 'Unspecified', 'EndpointKeysError',
     'QuotaExceeded', 'QnaRuntimeError', 'SKULimitExceeded',
     'OperationNotFound', 'ServiceError', 'ValidationFailure',
     'ExtractionFailure'
    :type code: str or
     ~azure.cognitiveservices.knowledge.qnamaker.runtime.models.ErrorCodeType
    :param message: A human-readable representation of the error.
    :type message: str
    :param target: The target of the error.
    :type target: str
    :param details: An array of details about specific errors that led to this
     reported error.
    :type details:
     list[~azure.cognitiveservices.knowledge.qnamaker.runtime.models.Error]
    :param inner_error: An object containing more specific information than
     the current object about the error.
    :type inner_error:
     ~azure.cognitiveservices.knowledge.qnamaker.runtime.models.InnerErrorModel
    """

    _validation = {
        'code': {'required': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'details': {'key': 'details', 'type': '[Error]'},
        'inner_error': {'key': 'innerError', 'type': 'InnerErrorModel'},
    }

    def __init__(self, *, code, message: str=None, target: str=None, details=None, inner_error=None, **kwargs) -> None:
        super(Error, self).__init__(**kwargs)
        self.code = code
        self.message = message
        self.target = target
        self.details = details
        self.inner_error = inner_error


class ErrorResponse(Model):
    """Error response. As per Microsoft One API guidelines -
    https://github.com/Microsoft/api-guidelines/blob/vNext/Guidelines.md#7102-error-condition-responses.

    :param error: The error object.
    :type error:
     ~azure.cognitiveservices.knowledge.qnamaker.runtime.models.ErrorResponseError
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorResponseError'},
    }

    def __init__(self, *, error=None, **kwargs) -> None:
        super(ErrorResponse, self).__init__(**kwargs)
        self.error = error


class ErrorResponseException(HttpOperationError):
    """Server responsed with exception of type: 'ErrorResponse'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(ErrorResponseException, self).__init__(deserialize, response, 'ErrorResponse', *args)


class ErrorResponseError(Error):
    """The error object.

    All required parameters must be populated in order to send to Azure.

    :param code: Required. One of a server-defined set of error codes.
     Possible values include: 'BadArgument', 'Forbidden', 'NotFound',
     'KbNotFound', 'Unauthorized', 'Unspecified', 'EndpointKeysError',
     'QuotaExceeded', 'QnaRuntimeError', 'SKULimitExceeded',
     'OperationNotFound', 'ServiceError', 'ValidationFailure',
     'ExtractionFailure'
    :type code: str or
     ~azure.cognitiveservices.knowledge.qnamaker.runtime.models.ErrorCodeType
    :param message: A human-readable representation of the error.
    :type message: str
    :param target: The target of the error.
    :type target: str
    :param details: An array of details about specific errors that led to this
     reported error.
    :type details:
     list[~azure.cognitiveservices.knowledge.qnamaker.runtime.models.Error]
    :param inner_error: An object containing more specific information than
     the current object about the error.
    :type inner_error:
     ~azure.cognitiveservices.knowledge.qnamaker.runtime.models.InnerErrorModel
    """

    _validation = {
        'code': {'required': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'details': {'key': 'details', 'type': '[Error]'},
        'inner_error': {'key': 'innerError', 'type': 'InnerErrorModel'},
    }

    def __init__(self, *, code, message: str=None, target: str=None, details=None, inner_error=None, **kwargs) -> None:
        super(ErrorResponseError, self).__init__(code=code, message=message, target=target, details=details, inner_error=inner_error, **kwargs)


class FeedbackRecordDTO(Model):
    """Active learning feedback record.

    :param user_id: Unique identifier for the user.
    :type user_id: str
    :param user_question: The suggested question being provided as feedback.
    :type user_question: str
    :param qna_id: The qnaId for which the suggested question is provided as
     feedback.
    :type qna_id: int
    """

    _validation = {
        'user_question': {'max_length': 1000},
    }

    _attribute_map = {
        'user_id': {'key': 'userId', 'type': 'str'},
        'user_question': {'key': 'userQuestion', 'type': 'str'},
        'qna_id': {'key': 'qnaId', 'type': 'int'},
    }

    def __init__(self, *, user_id: str=None, user_question: str=None, qna_id: int=None, **kwargs) -> None:
        super(FeedbackRecordDTO, self).__init__(**kwargs)
        self.user_id = user_id
        self.user_question = user_question
        self.qna_id = qna_id


class FeedbackRecordsDTO(Model):
    """Active learning feedback records.

    :param feedback_records: List of feedback records.
    :type feedback_records:
     list[~azure.cognitiveservices.knowledge.qnamaker.runtime.models.FeedbackRecordDTO]
    """

    _attribute_map = {
        'feedback_records': {'key': 'feedbackRecords', 'type': '[FeedbackRecordDTO]'},
    }

    def __init__(self, *, feedback_records=None, **kwargs) -> None:
        super(FeedbackRecordsDTO, self).__init__(**kwargs)
        self.feedback_records = feedback_records


class InnerErrorModel(Model):
    """An object containing more specific information about the error. As per
    Microsoft One API guidelines -
    https://github.com/Microsoft/api-guidelines/blob/vNext/Guidelines.md#7102-error-condition-responses.

    :param code: A more specific error code than was provided by the
     containing error.
    :type code: str
    :param inner_error: An object containing more specific information than
     the current object about the error.
    :type inner_error:
     ~azure.cognitiveservices.knowledge.qnamaker.runtime.models.InnerErrorModel
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'inner_error': {'key': 'innerError', 'type': 'InnerErrorModel'},
    }

    def __init__(self, *, code: str=None, inner_error=None, **kwargs) -> None:
        super(InnerErrorModel, self).__init__(**kwargs)
        self.code = code
        self.inner_error = inner_error


class MetadataDTO(Model):
    """Name - value pair of metadata.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. Metadata name.
    :type name: str
    :param value: Required. Metadata value.
    :type value: str
    """

    _validation = {
        'name': {'required': True, 'max_length': 100, 'min_length': 1},
        'value': {'required': True, 'max_length': 500, 'min_length': 1},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
    }

    def __init__(self, *, name: str, value: str, **kwargs) -> None:
        super(MetadataDTO, self).__init__(**kwargs)
        self.name = name
        self.value = value


class PromptDTO(Model):
    """Prompt for an answer.

    :param display_order: Index of the prompt - used in ordering of the
     prompts
    :type display_order: int
    :param qna_id: Qna id corresponding to the prompt - if QnaId is present,
     QnADTO object is ignored.
    :type qna_id: int
    :param qna: QnADTO - Either QnaId or QnADTO needs to be present in a
     PromptDTO object
    :type qna:
     ~azure.cognitiveservices.knowledge.qnamaker.runtime.models.PromptDTOQna
    :param display_text: Text displayed to represent a follow up question
     prompt
    :type display_text: str
    """

    _validation = {
        'display_text': {'max_length': 200},
    }

    _attribute_map = {
        'display_order': {'key': 'displayOrder', 'type': 'int'},
        'qna_id': {'key': 'qnaId', 'type': 'int'},
        'qna': {'key': 'qna', 'type': 'PromptDTOQna'},
        'display_text': {'key': 'displayText', 'type': 'str'},
    }

    def __init__(self, *, display_order: int=None, qna_id: int=None, qna=None, display_text: str=None, **kwargs) -> None:
        super(PromptDTO, self).__init__(**kwargs)
        self.display_order = display_order
        self.qna_id = qna_id
        self.qna = qna
        self.display_text = display_text


class QnADTO(Model):
    """Q-A object.

    All required parameters must be populated in order to send to Azure.

    :param id: Unique id for the Q-A.
    :type id: int
    :param answer: Required. Answer text
    :type answer: str
    :param source: Source from which Q-A was indexed. eg.
     https://docs.microsoft.com/en-us/azure/cognitive-services/QnAMaker/FAQs
    :type source: str
    :param questions: Required. List of questions associated with the answer.
    :type questions: list[str]
    :param metadata: List of metadata associated with the answer.
    :type metadata:
     list[~azure.cognitiveservices.knowledge.qnamaker.runtime.models.MetadataDTO]
    :param context: Context of a QnA
    :type context:
     ~azure.cognitiveservices.knowledge.qnamaker.runtime.models.QnADTOContext
    """

    _validation = {
        'answer': {'required': True, 'max_length': 25000, 'min_length': 1},
        'source': {'max_length': 300},
        'questions': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'answer': {'key': 'answer', 'type': 'str'},
        'source': {'key': 'source', 'type': 'str'},
        'questions': {'key': 'questions', 'type': '[str]'},
        'metadata': {'key': 'metadata', 'type': '[MetadataDTO]'},
        'context': {'key': 'context', 'type': 'QnADTOContext'},
    }

    def __init__(self, *, answer: str, questions, id: int=None, source: str=None, metadata=None, context=None, **kwargs) -> None:
        super(QnADTO, self).__init__(**kwargs)
        self.id = id
        self.answer = answer
        self.source = source
        self.questions = questions
        self.metadata = metadata
        self.context = context


class PromptDTOQna(QnADTO):
    """QnADTO - Either QnaId or QnADTO needs to be present in a PromptDTO object.

    All required parameters must be populated in order to send to Azure.

    :param id: Unique id for the Q-A.
    :type id: int
    :param answer: Required. Answer text
    :type answer: str
    :param source: Source from which Q-A was indexed. eg.
     https://docs.microsoft.com/en-us/azure/cognitive-services/QnAMaker/FAQs
    :type source: str
    :param questions: Required. List of questions associated with the answer.
    :type questions: list[str]
    :param metadata: List of metadata associated with the answer.
    :type metadata:
     list[~azure.cognitiveservices.knowledge.qnamaker.runtime.models.MetadataDTO]
    :param context: Context of a QnA
    :type context:
     ~azure.cognitiveservices.knowledge.qnamaker.runtime.models.QnADTOContext
    """

    _validation = {
        'answer': {'required': True, 'max_length': 25000, 'min_length': 1},
        'source': {'max_length': 300},
        'questions': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'answer': {'key': 'answer', 'type': 'str'},
        'source': {'key': 'source', 'type': 'str'},
        'questions': {'key': 'questions', 'type': '[str]'},
        'metadata': {'key': 'metadata', 'type': '[MetadataDTO]'},
        'context': {'key': 'context', 'type': 'QnADTOContext'},
    }

    def __init__(self, *, answer: str, questions, id: int=None, source: str=None, metadata=None, context=None, **kwargs) -> None:
        super(PromptDTOQna, self).__init__(id=id, answer=answer, source=source, questions=questions, metadata=metadata, context=context, **kwargs)


class QnADTOContext(ContextDTO):
    """Context of a QnA.

    :param is_context_only: To mark if a prompt is relevant only with a
     previous question or not.
     true - Do not include this QnA as search result for queries without
     context
     false - ignores context and includes this QnA in search result
    :type is_context_only: bool
    :param prompts: List of prompts associated with the answer.
    :type prompts:
     list[~azure.cognitiveservices.knowledge.qnamaker.runtime.models.PromptDTO]
    """

    _validation = {
        'prompts': {'max_items': 20},
    }

    _attribute_map = {
        'is_context_only': {'key': 'isContextOnly', 'type': 'bool'},
        'prompts': {'key': 'prompts', 'type': '[PromptDTO]'},
    }

    def __init__(self, *, is_context_only: bool=None, prompts=None, **kwargs) -> None:
        super(QnADTOContext, self).__init__(is_context_only=is_context_only, prompts=prompts, **kwargs)


class QnASearchResult(Model):
    """Represents Search Result.

    :param questions: List of questions.
    :type questions: list[str]
    :param answer: Answer.
    :type answer: str
    :param score: Search result score.
    :type score: float
    :param id: Id of the QnA result.
    :type id: int
    :param source: Source of QnA result.
    :type source: str
    :param metadata: List of metadata.
    :type metadata:
     list[~azure.cognitiveservices.knowledge.qnamaker.runtime.models.MetadataDTO]
    :param context: Context object of the QnA
    :type context:
     ~azure.cognitiveservices.knowledge.qnamaker.runtime.models.QnASearchResultContext
    """

    _attribute_map = {
        'questions': {'key': 'questions', 'type': '[str]'},
        'answer': {'key': 'answer', 'type': 'str'},
        'score': {'key': 'score', 'type': 'float'},
        'id': {'key': 'id', 'type': 'int'},
        'source': {'key': 'source', 'type': 'str'},
        'metadata': {'key': 'metadata', 'type': '[MetadataDTO]'},
        'context': {'key': 'context', 'type': 'QnASearchResultContext'},
    }

    def __init__(self, *, questions=None, answer: str=None, score: float=None, id: int=None, source: str=None, metadata=None, context=None, **kwargs) -> None:
        super(QnASearchResult, self).__init__(**kwargs)
        self.questions = questions
        self.answer = answer
        self.score = score
        self.id = id
        self.source = source
        self.metadata = metadata
        self.context = context


class QnASearchResultContext(ContextDTO):
    """Context object of the QnA.

    :param is_context_only: To mark if a prompt is relevant only with a
     previous question or not.
     true - Do not include this QnA as search result for queries without
     context
     false - ignores context and includes this QnA in search result
    :type is_context_only: bool
    :param prompts: List of prompts associated with the answer.
    :type prompts:
     list[~azure.cognitiveservices.knowledge.qnamaker.runtime.models.PromptDTO]
    """

    _validation = {
        'prompts': {'max_items': 20},
    }

    _attribute_map = {
        'is_context_only': {'key': 'isContextOnly', 'type': 'bool'},
        'prompts': {'key': 'prompts', 'type': '[PromptDTO]'},
    }

    def __init__(self, *, is_context_only: bool=None, prompts=None, **kwargs) -> None:
        super(QnASearchResultContext, self).__init__(is_context_only=is_context_only, prompts=prompts, **kwargs)


class QnASearchResultList(Model):
    """Represents List of Question Answers.

    :param answers: Represents Search Result list.
    :type answers:
     list[~azure.cognitiveservices.knowledge.qnamaker.runtime.models.QnASearchResult]
    """

    _attribute_map = {
        'answers': {'key': 'answers', 'type': '[QnASearchResult]'},
    }

    def __init__(self, *, answers=None, **kwargs) -> None:
        super(QnASearchResultList, self).__init__(**kwargs)
        self.answers = answers


class QueryContextDTO(Model):
    """Context object with previous QnA's information.

    :param previous_qna_id: Previous QnA Id - qnaId of the top result.
    :type previous_qna_id: str
    :param previous_user_query: Previous user query.
    :type previous_user_query: str
    """

    _attribute_map = {
        'previous_qna_id': {'key': 'previousQnaId', 'type': 'str'},
        'previous_user_query': {'key': 'previousUserQuery', 'type': 'str'},
    }

    def __init__(self, *, previous_qna_id: str=None, previous_user_query: str=None, **kwargs) -> None:
        super(QueryContextDTO, self).__init__(**kwargs)
        self.previous_qna_id = previous_qna_id
        self.previous_user_query = previous_user_query


class QueryDTO(Model):
    """POST body schema to query the knowledgebase.

    :param qna_id: Exact qnaId to fetch from the knowledgebase, this field
     takes priority over question.
    :type qna_id: str
    :param question: User question to query against the knowledge base.
    :type question: str
    :param top: Max number of answers to be returned for the question.
    :type top: int
    :param user_id: Unique identifier for the user. Optional parameter for
     telemetry. For more information, refer <a
     href="http://aka.ms/qnamaker-analytics#user-traffic"
     target="blank">Analytics and Telemetry</a>.
    :type user_id: str
    :param is_test: Query against the test index.
    :type is_test: bool
    :param score_threshold: Threshold for answers returned based on score.
    :type score_threshold: float
    :param context: Context object with previous QnA's information.
    :type context:
     ~azure.cognitiveservices.knowledge.qnamaker.runtime.models.QueryDTOContext
    :param ranker_type: Optional field. Set to 'QuestionOnly' for using a
     question only Ranker.
    :type ranker_type: str
    :param strict_filters: Find only answers that contain these metadata.
    :type strict_filters:
     list[~azure.cognitiveservices.knowledge.qnamaker.runtime.models.MetadataDTO]
    :param strict_filters_compound_operation_type: Optional field. Set to OR
     for using OR as Operation for Strict Filters. Possible values include:
     'AND', 'OR'
    :type strict_filters_compound_operation_type: str or
     ~azure.cognitiveservices.knowledge.qnamaker.runtime.models.StrictFiltersCompoundOperationType
    """

    _attribute_map = {
        'qna_id': {'key': 'qnaId', 'type': 'str'},
        'question': {'key': 'question', 'type': 'str'},
        'top': {'key': 'top', 'type': 'int'},
        'user_id': {'key': 'userId', 'type': 'str'},
        'is_test': {'key': 'isTest', 'type': 'bool'},
        'score_threshold': {'key': 'scoreThreshold', 'type': 'float'},
        'context': {'key': 'context', 'type': 'QueryDTOContext'},
        'ranker_type': {'key': 'rankerType', 'type': 'str'},
        'strict_filters': {'key': 'strictFilters', 'type': '[MetadataDTO]'},
        'strict_filters_compound_operation_type': {'key': 'strictFiltersCompoundOperationType', 'type': 'str'},
    }

    def __init__(self, *, qna_id: str=None, question: str=None, top: int=None, user_id: str=None, is_test: bool=None, score_threshold: float=None, context=None, ranker_type: str=None, strict_filters=None, strict_filters_compound_operation_type=None, **kwargs) -> None:
        super(QueryDTO, self).__init__(**kwargs)
        self.qna_id = qna_id
        self.question = question
        self.top = top
        self.user_id = user_id
        self.is_test = is_test
        self.score_threshold = score_threshold
        self.context = context
        self.ranker_type = ranker_type
        self.strict_filters = strict_filters
        self.strict_filters_compound_operation_type = strict_filters_compound_operation_type


class QueryDTOContext(QueryContextDTO):
    """Context object with previous QnA's information.

    :param previous_qna_id: Previous QnA Id - qnaId of the top result.
    :type previous_qna_id: str
    :param previous_user_query: Previous user query.
    :type previous_user_query: str
    """

    _attribute_map = {
        'previous_qna_id': {'key': 'previousQnaId', 'type': 'str'},
        'previous_user_query': {'key': 'previousUserQuery', 'type': 'str'},
    }

    def __init__(self, *, previous_qna_id: str=None, previous_user_query: str=None, **kwargs) -> None:
        super(QueryDTOContext, self).__init__(previous_qna_id=previous_qna_id, previous_user_query=previous_user_query, **kwargs)
