# The Matching Game
- Who is requesting access?
- How and what do they want to access?
- Analyzing the authorization context


# Attributes and Tagging
- Attribute-based access control (ABAC) is an authorization strategy that defines permissions based on attributes. In AWS, these attributes are called tags. You can create a single ABAC policy or small set of policies for your IAM principals. These ABAC policies can be designed to allow operations when the principal's tag matches the resource tag
https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_attribute-based-access-control.html
- Benefits of the ABAC method
  - Scalable
  - manageable
  - granular permissions
  
