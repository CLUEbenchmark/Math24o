import os
import pandas as pd

def extract_final_answer(each_mod_answer):
    """提取待测模型回答中 \boxed{} 中的内容，如果待测模型没有根据要求使用 \boxed{} 的格式输出最终答案，则返回空字符串
    params:
        each_mod_answer: 待测模型给出的回答
    return:
        each_final_answer：\boxed{} 中的内容"""

    start_index = 0
    end_index = 0

    each_mod_answer = repr(each_mod_answer)

    if not each_mod_answer or each_mod_answer == '' or each_mod_answer == None:
        each_final_answer = ''
        return each_final_answer

    for i in range(0, len(each_mod_answer)):
            if end_index != 0:
                try:
                    if each_mod_answer[-i-2] == 'd' and each_mod_answer[-i-3] == 'e' and each_mod_answer[-i-4] == 'x' and each_mod_answer[-i-5] == 'o':
                        start_index = -i
                        break
                    else:
                        continue
                except:
                    return ''

            
            else:
                if each_mod_answer[-i] == '}':
                    end_index = -i
                else:
                    continue
        
    each_final_answer = each_mod_answer[start_index:end_index]

    i = 0

    while i <= len(each_final_answer):
        try: 
            if each_final_answer[i] == '\\' and each_final_answer[i+1] == '\\':
                each_final_answer = each_final_answer[:i] + each_final_answer[i+1:]
        except:
            i += 1
            continue

        i += 1

    return each_final_answer

def auto_gene_evaluation_result():

    #---------- initial config ----------#

    current_dir = os.path.dirname(os.path.realpath(__file__))

    #---#

    questions_file_path = os.path.join(current_dir, 'math24o.xlsx')
    questions_dataframe = pd.read_excel(questions_file_path)

    mod_answers_file_path = os.path.join(current_dir, 'model_answers.xlsx')
    mod_answers_dataframe = pd.read_excel(mod_answers_file_path)

    id_list = questions_dataframe['id']
    question_list = questions_dataframe['questions']
    ref_answer_list = questions_dataframe['ref_answers']
    mod_answer_list = mod_answers_dataframe['model_answers']

    output_dataframe = pd.DataFrame({})

    count = 1

    #---------- essential loop ----------#

    for each_id, each_question, each_ref_answer, each_mod_answer in zip(id_list, question_list, ref_answer_list, mod_answer_list):

        each_final_answer = extract_final_answer(each_mod_answer)

        try: 
            each_final_answer = float(each_final_answer)
        except:
            each_final_answer = each_final_answer


        if each_final_answer == each_ref_answer:
            each_score = 1
        else:
            # print(type(each_ref_answer), type(each_final_answer))
            each_score = 0

        #---------- output processing message ----------#

        # match str(count)[-1]:
        #     case '1':
        #         print(">>> Evaluating " + str(count) + "st model's answer...")
        #     case '2':
        #         print(">>> Evaluating " + str(count) + "nd model's answer...")
        #     case '3':
        #         print(">>> Evaluating " + str(count) + "rd model's answer...")
        #     case _:
        #         print(">>> Evaluating " + str(count) + "th model's answer...")

        #---------- for developer ----------#

        new_dataframe = pd.DataFrame({'id': [each_id], 'questions': [each_question], 'ref_answers': [each_ref_answer], 'mod_answers': [each_mod_answer], 'final_answers':[each_final_answer], 'scores':[each_score]})

        #---------- for user ----------#

        # new_dataframe = pd.DataFrame({'id': [each_id], 'mod_answers': [each_mod_answer], 'scores':[each_score]})

        #---------- preparation of output ----------#

        output_dataframe = pd.concat([output_dataframe, new_dataframe], ignore_index=True)

        output_file_path = os.path.join(current_dir, 'output.xlsx')

        output_dataframe.to_excel(output_file_path, index=False)

        #---------- output successfull message ----------#

        match str(count)[-1]:
            case '1':
                print(">>> " + str(count) +
                      "st model's answer has been evaluated successfully.")
            case '2':
                print(">>> " + str(count) +
                      "nd model's answer has been evaluated successfully.")
            case '3':
                print(">>> " + str(count) +
                      "rd model's answer has been evaluated successfully.")
            case _:
                print(">>> " + str(count) +
                      "th model's answer has been evaluated successfully.")

        #---------- after an evaluation, add 1 to count ----------#

        count += 1

        #----------------------------------------------#

    score_list = output_dataframe['scores']

    average = sum(score_list) / len(score_list)

    average_dataframe = pd.DataFrame({'scores':[100*average]})
    output_dataframe = pd.concat([output_dataframe, average_dataframe], ignore_index=True)

    output_dataframe.to_excel(output_file_path, index=False)

    print(">>> All model's answers have been evaluated successfully! The final score is " + str(100*average) + '. For more evaluation details, please check the output.xlsx file.')

if __name__ == '__main__':

    auto_gene_evaluation_result()