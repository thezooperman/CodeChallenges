# job_recommendation.py

import json
import glob


class JobType():
    def __init__(self):
        self.type = ''
        self.skillOrder = dict()


class ApplicantProfile():
    def __init__(self, skillOrder, jobId, jobName):
        self.skillOrder = skillOrder
        self.jobId = jobId
        self.jobName = jobName

    def __repr__(self):
        return "Applicant Skill(s): %s" % self.skillOrder


class JobScore():
    def __init__(self, jobType, score, skillRank, jobId):
        self.jobType = jobType
        self.score = score
        self.skillRank = skillRank
        self.jobId = jobId

    def __repr__(self):
        return "Job Type:%s Job Score:%d Skills:%s" %\
            (self.jobType, self.score, self.skillRank)


class Main():
    def __init__(self):
        self.jobTypes = list()
        self.scores = []
        self.applicationProfile = ApplicantProfile
        self.counter = 0

    def populateJobTypeFromFile(self, fileName):
        data = None
        with open(fileName) as f:
            data = json.load(f)
        for jtype, skills in data.items():
            tmp = JobType()
            tmp.type = jtype
            rank = 1
            # data clean up from source file
            for val in skills:
                if str.find(val, ' '):
                    val = str.replace(val, ' ', '_').lower()
                    tmp.skillOrder.setdefault(val, rank)
                    rank += 1
            self.jobTypes.append(tmp)

    def buildApplicantSkillProfile(self, applicantFile):
        data = None
        with open(applicantFile) as f:
            data = json.load(f)
            skills = data['appln_skills']
            self.applicationProfile = ApplicantProfile({}, data['appln_num'],
                                                       data['appln_name'])
            rank = 1
            # data cleanup from source file
            for val in skills:
                if str.find(val, ' '):
                    val = str.replace(val, ' ', '_').lower()
                    self.applicationProfile.skillOrder.setdefault(val, rank)
                    rank += 1

    def buildScoreFromProfile(self):
        skills = self.applicationProfile.skillOrder
        #  build the scores from applicant profile and job profile
        for jtypes in self.jobTypes:
            matchingJob = jtypes.skillOrder
            score = JobScore(jtypes.type, 0, dict(),
                             self.applicationProfile.jobId)
            for skill in skills:
                if skill in matchingJob:
                    score.skillRank.setdefault(
                        # skills[skill] - matchingJob[skill])
                        skill, matchingJob[skill])
                    score.score += 1  # abs(skills[skill] - matchingJob[skill])
            if score.score > 0:
                self.scores.append(score)
        # In-case of job match with same score, compare and
        # pick the job score with minimum skill rank
        s = sorted(self.scores, key=lambda x: x.score, reverse=True)
        max_score = s[0].score
        filtered_by_max_score = [score for score in s if
                                 score.score == max_score]
        min_val = None
        s = None
        for v in filtered_by_max_score:
            val = min(v.skillRank.values())
            if min_val is None:
                min_val = val
                s = v
            elif val < min_val:
                s = v
        if s is not None:
            self.counter += 1
            print('#:%d JobId:%s - Recommened Job:%s' %
                  (self.counter, s.jobId, s.jobType.upper()))
        else:
            print('No recommended job for applicant id:',
                  self.applicationProfile.jobId)
        self.scores.clear()


def main():
    obj = Main()
    obj.populateJobTypeFromFile(
        '/home/aritraghosh/Downloads/job_skills_reco_gen-2/' +
        'job_requirements.json')
    for f in glob.glob('/home/aritraghosh/Downloads/job_skills_reco_gen-2' +
                       '/appln_*.json'):
        obj.buildApplicantSkillProfile(f)
        obj.buildScoreFromProfile()


if __name__ == '__main__':
    main()
