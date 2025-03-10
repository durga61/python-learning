import boto3


def list_vpc_dependents(region_name):
    ec2_client = boto3.client("ec2", region_name=region_name)

    vpcs = ec2_client.describe_vpcs()["Vpcs"]
    print("describe vpc dependents")
    print("pr testing ")
    for vpc in vpcs:
        vpc_id = vpc["VpcId"]
        print(f"VPC ID: {vpc_id}")

        # List comprehensions for fetching resources
        subnets = ec2_client.describe_subnets(
            Filters=[{"Name": "vpc-id", "Values": [vpc_id]}]
        )["Subnets"]
        print(f"  Subnets: {[subnet['SubnetId'] for subnet in subnets]}")

        security_groups = ec2_client.describe_security_groups(
            Filters=[{"Name": "vpc-id", "Values": [vpc_id]}]
        )["SecurityGroups"]
        print(f"  Security Groups: {[sg['GroupId'] for sg in security_groups]}")

        route_tables = ec2_client.describe_route_tables(
            Filters=[{"Name": "vpc-id", "Values": [vpc_id]}]
        )["RouteTables"]
        print(f"  Route Tables: {[rt['RouteTableId'] for rt in route_tables]}")

        internet_gateways = ec2_client.describe_internet_gateways(
            Filters=[{"Name": "attachment.vpc-id", "Values": [vpc_id]}]
        )["InternetGateways"]
        print(
            f"  Internet Gateways: {[ig['InternetGatewayId'] for ig in internet_gateways]}"
        )

        nat_gateways = ec2_client.describe_nat_gateways(
            Filters=[{"Name": "vpc-id", "Values": [vpc_id]}]
        )["NatGateways"]
        print(f"  NAT Gateways: {[ng['NatGatewayId'] for ng in nat_gateways]}")

        network_acls = ec2_client.describe_network_acls(
            Filters=[{"Name": "vpc-id", "Values": [vpc_id]}]
        )["NetworkAcls"]
        print(f"  Network ACLs: {[nacl['NetworkAclId'] for nacl in network_acls]}")

        dhcp_options = ec2_client.describe_dhcp_options()["DhcpOptions"]
        vpc_dhcp_options = [
            dhcp["DhcpOptionsId"]
            for dhcp in dhcp_options
            if dhcp["DhcpOptionsId"] in vpc["DhcpOptionsId"]
        ]
        print(f"  DHCP Options: {vpc_dhcp_options}")

        print()  # Blank line between VPCs


# Specify the AWS region you want to query
region = "us-west-1"  # Change this to your desired region
list_vpc_dependents(region)
