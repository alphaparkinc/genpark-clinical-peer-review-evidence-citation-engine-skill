from client import ClinicalPeerReviewEvidenceCitationEngineClient

def main():
    client = ClinicalPeerReviewEvidenceCitationEngineClient()
    res = client.synthesize_clinical_consensus_evidence('Comparison of SGLT2 inhibitors vs GLP-1 RA in chronic kidney disease stage 3b')
    print('Evidence ID: ' + res['evidence_query_id'] + ' (Analyzed ' + str(res['peer_reviewed_rcts_analyzed']) + ' RCTs)')
    print('Citations: ' + ', '.join(res['top_medical_journal_citations']))
    print('Guideline Score: ' + str(res['fda_ema_guideline_alignment_score_pct']) + '% | Alerts: ' + ', '.join(res['contraindication_alerts_surfaced']))

if __name__ == '__main__':
    main()
