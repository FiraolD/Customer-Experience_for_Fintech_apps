import pytest
import pandas as pd
from datetime import datetime
import re
import os
from src.database import safe_convert_to_numeric, validate_row

class TestDataProcessing(pytest):

    def test_safe_convert_to_numeric(self):
        self.assertEqual(safe_convert_to_numeric("5"), 5)
        self.assertEqual(safe_convert_to_numeric("3.7"), 3)
        self.assertEqual(safe_convert_to_numeric(None), 0)
        self.assertEqual(safe_convert_to_numeric("abc"), 0)

    def test_validate_row_valid(self):
        expected_columns = [
            'reviewId', 'userName', 'userImage', 'content1',
            'score', 'thumbsUpCount', 'reviewCreatedVersion', 'DateAt',
            'replyContent', 'repliedAt', 'appVersion', 'bank',
            'cleanedat', 'cleaned_content', 'sentiment', 'keywords', 'theme'
        ]
        row = pd.Series([
            "id1", "User A", "", "Good app", "5", "2",
            "1.0.0", "12/12/2024 10:00", "", "12/12/2024",
            "v1", "CBE", "12/12/2024", "cleaned", "positive", "[]", "other"
        ], index=expected_columns)

        validated_row = validate_row(row)
        self.assertIsNotNone(validated_row)
        self.assertIsInstance(validated_row['score'], int)
        self.assertIsInstance(validated_row['thumbsUpCount'], int)
        self.assertIsInstance(validated_row['DateAt'], datetime)

    def test_validate_row_invalid_score(self):
        expected_columns = [
            'reviewId', 'userName', 'userImage', 'content1',
            'score', 'thumbsUpCount', 'reviewCreatedVersion', 'DateAt',
            'replyContent', 'repliedAt', 'appVersion', 'bank',
            'cleanedat', 'cleaned_content', 'sentiment', 'keywords', 'theme'
        ]
        row = pd.Series([
            "id1", "User A", "", "Good app", "invalid_score", "2",
            "1.0.0", "12/12/2024 10:00", "", "12/12/2024",
            "v1", "CBE", "12/12/2024", "cleaned", "positive", "[]", "other"
        ], index=expected_columns)

        validated_row = validate_row(row)
        self.assertIsNone(validated_row)  # Should fail due to invalid score

    def test_date_parsing(self):
        expected_columns = [
            'reviewId', 'userName', 'userImage', 'content1',
            'score', 'thumbsUpCount', 'reviewCreatedVersion', 'DateAt',
            'replyContent', 'repliedAt', 'appVersion', 'bank',
            'cleanedat', 'cleaned_content', 'sentiment', 'keywords', 'theme'
        ]
        row = pd.Series([
            "id1", "User A", "", "Good app", "5", "2",
            "1.0.0", "12/12/2024", "", "12/12/2024",
            "v1", "CBE", "12/12/2024", "cleaned", "positive", "[]", "other"
        ], index=expected_columns)

        validated_row = validate_row(row)
        self.assertIsInstance(validated_row['DateAt'], datetime)

    def test_missing_required_fields(self):
        expected_columns = [
            'reviewId', 'userName', 'userImage', 'content1',
            'score', 'thumbsUpCount', 'reviewCreatedVersion', 'DateAt',
            'replyContent', 'repliedAt', 'appVersion', 'bank',
            'cleanedat', 'cleaned_content', 'sentiment', 'keywords', 'theme'
        ]
        row = pd.Series([
            None, None, "", "Good app", "5", "2",
            "1.0.0", "12/12/2024", "", "12/12/2024",
            "v1", "CBE", "12/12/2024", "cleaned", "positive", "[]", "other"
        ], index=expected_columns)

        validated_row = validate_row(row)
        self.assertIsNone(validated_row)  # Should fail due to missing required fields


if __name__ == '__main__':
    pytest.main()
    