from django.test import TestCase
from members.models import MembershipPlan, Member, Membership


# Create your tests here.



class TestModels(TestCase):
    fixtures = ["member.json", "membership.json","membershipplan.json","user.json"]

    def test_should_create_membershipplan(self):
        membershipplan = MembershipPlan.objects.get(pk=1)
        self.assertEqual(membershipplan.plan_name, "Yearly Individual")

    def test_should_create_member(self):
        member = Member.objects.get(pk=1)
        self.assertEqual(member.first_name, "Dinusha")

    def test_should_create_membership(self):
        membership = Membership.objects.get(pk=1)
        self.assertEqual(membership.final_fee.__str__(), "1000.00")