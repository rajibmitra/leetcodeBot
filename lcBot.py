### code to get the leetcode daily question


import requests
import json
import time
import os
import sys


def get_question(question_id):
    url = 'https://leetcode.com/graphql'
    query = '''
    query Question($questionId: Int!) {
      question(questionId: $questionId) {
        questionId
        title
        content
        stats {
          totalAccepted
          totalSubmissions
          totalSubscribers
        }
        solution {
          lang
          url
        }
        tags {
          name
        }
        similarQuestions {
          questionId
          title
        }
      }
    }
    '''
    variables = {'questionId': question_id}
    data = {'query': query, 'variables': variables}
    r = requests.post(url, data=json.dumps(data))
    return r.json()['data']['question']


def get_question_list(page):    
    url = 'https://leetcode.com/graphql'
    query = '''
    query List($page: Int!) {
      questionList(page: $page) {
        hasNextPage
        questions {
          questionId
          title
          content
          stats {
            totalAccepted
            totalSubmissions
            totalSubscribers
          }
          solution {
            lang
            url
          }
          tags {
            name
          }
          similarQuestions {
            questionId
            title
          }
        }
      }
    }
    '''
    variables = {'page': page}
    data = {'query': query, 'variables': variables}
    r = requests.post(url, data=json.dumps(data))
    return r.json()['data']['questionList']


def get_question_list_by_tag(tag, page):
    url = 'https://leetcode.com/graphql'
    query = '''
    query List($tag: String!, $page: Int!) {
      questionListByTag(tag: $tag, page: $page) {
        hasNextPage
        questions {
          questionId
          title
          content
          stats {
            totalAccepted
            totalSubmissions
            totalSubscribers
          }
          solution {
            lang
            url
          }
          tags {
            name
          }
          similarQuestions {
            questionId
            title
          }
        }
      }
    }
    '''
    variables = {'tag': tag, 'page': page}
    data = {'query': query, 'variables': variables}
    r = requests.post(url, data=json.dumps(data))
    return r.json()['data']['questionListByTag']




if __name__ == '__main__':
    # get_question(question_id)
    # get_question_list(page)
    # get_question_list_by_tag(tag, page)
    pass
    # print(get_question_list_by_tag('array', 1))
    # print(get_question_list_by_tag('array', 2))s

 
