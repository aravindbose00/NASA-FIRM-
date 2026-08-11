import unittest

import numpy as np
import pandas as pd


class TestNASAAnalysis(unittest.TestCase):
    """Tests for NASA FIRMS data-analysis operations."""

    def setUp(self):
        """Create a small example FIRMS dataset for testing."""

        self.data = pd.DataFrame({
            "latitude": [10.0, 20.0, 30.0],
            "longitude": [40.0, 50.0, 60.0],
            "frp": [10.0, 20.0, 30.0],
            "daynight": ["D", "N", "D"],
            "acq_date": pd.to_datetime([
                "2024-01-01",
                "2024-01-15",
                "2024-02-01",
            ]),
        })

    def test_row_count(self):
        """Test whether the number of rows is correct."""

        self.assertEqual(len(self.data), 3)

    def test_frp_mean(self):
        """Test FRP mean calculation."""

        mean_frp = self.data["frp"].mean()

        self.assertAlmostEqual(mean_frp, 20.0)

    def test_frp_minimum(self):
        """Test FRP minimum calculation."""

        self.assertEqual(
            self.data["frp"].min(),
            10.0,
        )

    def test_frp_maximum(self):
        """Test FRP maximum calculation."""

        self.assertEqual(
            self.data["frp"].max(),
            30.0,
        )

    def test_daynight_counts(self):
        """Test day and night detection counts."""

        counts = self.data["daynight"].value_counts()

        self.assertEqual(counts["D"], 2)
        self.assertEqual(counts["N"], 1)

    def test_monthly_counts(self):
        """Test monthly fire-detection aggregation."""

        months = (
            self.data["acq_date"]
            .dt.to_period("M")
            .astype(str)
            .value_counts()
        )

        self.assertEqual(months["2024-01"], 2)
        self.assertEqual(months["2024-02"], 1)

    def test_positive_frp(self):
        """Check that example FRP observations are positive."""

        self.assertTrue(
            np.all(self.data["frp"] > 0)
        )


if __name__ == "__main__":
    unittest.main()
