# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.cloud.area120_tables_v1alpha1.proto import (
    tables_pb2 as google_dot_cloud_dot_area120__tables__v1alpha1_dot_proto_dot_tables__pb2,
)
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class TablesServiceStub(object):
    """The Tables Service provides an API for reading and updating tables.
    It defines the following resource model:

    - The API has a collection of [Table][google.area120.tables.v1alpha1.Table]
    resources, named `tables/*`

    - Each Table has a collection of [Row][google.area120.tables.v1alpha1.Row]
    resources, named `tables/*/rows/*`
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetTable = channel.unary_unary(
            "/google.area120.tables.v1alpha1.TablesService/GetTable",
            request_serializer=google_dot_cloud_dot_area120__tables__v1alpha1_dot_proto_dot_tables__pb2.GetTableRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_area120__tables__v1alpha1_dot_proto_dot_tables__pb2.Table.FromString,
        )
        self.ListTables = channel.unary_unary(
            "/google.area120.tables.v1alpha1.TablesService/ListTables",
            request_serializer=google_dot_cloud_dot_area120__tables__v1alpha1_dot_proto_dot_tables__pb2.ListTablesRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_area120__tables__v1alpha1_dot_proto_dot_tables__pb2.ListTablesResponse.FromString,
        )
        self.GetRow = channel.unary_unary(
            "/google.area120.tables.v1alpha1.TablesService/GetRow",
            request_serializer=google_dot_cloud_dot_area120__tables__v1alpha1_dot_proto_dot_tables__pb2.GetRowRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_area120__tables__v1alpha1_dot_proto_dot_tables__pb2.Row.FromString,
        )
        self.ListRows = channel.unary_unary(
            "/google.area120.tables.v1alpha1.TablesService/ListRows",
            request_serializer=google_dot_cloud_dot_area120__tables__v1alpha1_dot_proto_dot_tables__pb2.ListRowsRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_area120__tables__v1alpha1_dot_proto_dot_tables__pb2.ListRowsResponse.FromString,
        )
        self.CreateRow = channel.unary_unary(
            "/google.area120.tables.v1alpha1.TablesService/CreateRow",
            request_serializer=google_dot_cloud_dot_area120__tables__v1alpha1_dot_proto_dot_tables__pb2.CreateRowRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_area120__tables__v1alpha1_dot_proto_dot_tables__pb2.Row.FromString,
        )
        self.BatchCreateRows = channel.unary_unary(
            "/google.area120.tables.v1alpha1.TablesService/BatchCreateRows",
            request_serializer=google_dot_cloud_dot_area120__tables__v1alpha1_dot_proto_dot_tables__pb2.BatchCreateRowsRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_area120__tables__v1alpha1_dot_proto_dot_tables__pb2.BatchCreateRowsResponse.FromString,
        )
        self.UpdateRow = channel.unary_unary(
            "/google.area120.tables.v1alpha1.TablesService/UpdateRow",
            request_serializer=google_dot_cloud_dot_area120__tables__v1alpha1_dot_proto_dot_tables__pb2.UpdateRowRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_area120__tables__v1alpha1_dot_proto_dot_tables__pb2.Row.FromString,
        )
        self.BatchUpdateRows = channel.unary_unary(
            "/google.area120.tables.v1alpha1.TablesService/BatchUpdateRows",
            request_serializer=google_dot_cloud_dot_area120__tables__v1alpha1_dot_proto_dot_tables__pb2.BatchUpdateRowsRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_area120__tables__v1alpha1_dot_proto_dot_tables__pb2.BatchUpdateRowsResponse.FromString,
        )
        self.DeleteRow = channel.unary_unary(
            "/google.area120.tables.v1alpha1.TablesService/DeleteRow",
            request_serializer=google_dot_cloud_dot_area120__tables__v1alpha1_dot_proto_dot_tables__pb2.DeleteRowRequest.SerializeToString,
            response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )


class TablesServiceServicer(object):
    """The Tables Service provides an API for reading and updating tables.
    It defines the following resource model:

    - The API has a collection of [Table][google.area120.tables.v1alpha1.Table]
    resources, named `tables/*`

    - Each Table has a collection of [Row][google.area120.tables.v1alpha1.Row]
    resources, named `tables/*/rows/*`
    """

    def GetTable(self, request, context):
        """Gets a table. Returns NOT_FOUND if the table does not exist.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ListTables(self, request, context):
        """Lists tables for the user.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetRow(self, request, context):
        """Gets a row. Returns NOT_FOUND if the row does not exist in the table.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ListRows(self, request, context):
        """Lists rows in a table. Returns NOT_FOUND if the table does not exist.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def CreateRow(self, request, context):
        """Creates a row.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def BatchCreateRows(self, request, context):
        """Creates multiple rows.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def UpdateRow(self, request, context):
        """Updates a row.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def BatchUpdateRows(self, request, context):
        """Updates multiple rows.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeleteRow(self, request, context):
        """Deletes a row.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_TablesServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "GetTable": grpc.unary_unary_rpc_method_handler(
            servicer.GetTable,
            request_deserializer=google_dot_cloud_dot_area120__tables__v1alpha1_dot_proto_dot_tables__pb2.GetTableRequest.FromString,
            response_serializer=google_dot_cloud_dot_area120__tables__v1alpha1_dot_proto_dot_tables__pb2.Table.SerializeToString,
        ),
        "ListTables": grpc.unary_unary_rpc_method_handler(
            servicer.ListTables,
            request_deserializer=google_dot_cloud_dot_area120__tables__v1alpha1_dot_proto_dot_tables__pb2.ListTablesRequest.FromString,
            response_serializer=google_dot_cloud_dot_area120__tables__v1alpha1_dot_proto_dot_tables__pb2.ListTablesResponse.SerializeToString,
        ),
        "GetRow": grpc.unary_unary_rpc_method_handler(
            servicer.GetRow,
            request_deserializer=google_dot_cloud_dot_area120__tables__v1alpha1_dot_proto_dot_tables__pb2.GetRowRequest.FromString,
            response_serializer=google_dot_cloud_dot_area120__tables__v1alpha1_dot_proto_dot_tables__pb2.Row.SerializeToString,
        ),
        "ListRows": grpc.unary_unary_rpc_method_handler(
            servicer.ListRows,
            request_deserializer=google_dot_cloud_dot_area120__tables__v1alpha1_dot_proto_dot_tables__pb2.ListRowsRequest.FromString,
            response_serializer=google_dot_cloud_dot_area120__tables__v1alpha1_dot_proto_dot_tables__pb2.ListRowsResponse.SerializeToString,
        ),
        "CreateRow": grpc.unary_unary_rpc_method_handler(
            servicer.CreateRow,
            request_deserializer=google_dot_cloud_dot_area120__tables__v1alpha1_dot_proto_dot_tables__pb2.CreateRowRequest.FromString,
            response_serializer=google_dot_cloud_dot_area120__tables__v1alpha1_dot_proto_dot_tables__pb2.Row.SerializeToString,
        ),
        "BatchCreateRows": grpc.unary_unary_rpc_method_handler(
            servicer.BatchCreateRows,
            request_deserializer=google_dot_cloud_dot_area120__tables__v1alpha1_dot_proto_dot_tables__pb2.BatchCreateRowsRequest.FromString,
            response_serializer=google_dot_cloud_dot_area120__tables__v1alpha1_dot_proto_dot_tables__pb2.BatchCreateRowsResponse.SerializeToString,
        ),
        "UpdateRow": grpc.unary_unary_rpc_method_handler(
            servicer.UpdateRow,
            request_deserializer=google_dot_cloud_dot_area120__tables__v1alpha1_dot_proto_dot_tables__pb2.UpdateRowRequest.FromString,
            response_serializer=google_dot_cloud_dot_area120__tables__v1alpha1_dot_proto_dot_tables__pb2.Row.SerializeToString,
        ),
        "BatchUpdateRows": grpc.unary_unary_rpc_method_handler(
            servicer.BatchUpdateRows,
            request_deserializer=google_dot_cloud_dot_area120__tables__v1alpha1_dot_proto_dot_tables__pb2.BatchUpdateRowsRequest.FromString,
            response_serializer=google_dot_cloud_dot_area120__tables__v1alpha1_dot_proto_dot_tables__pb2.BatchUpdateRowsResponse.SerializeToString,
        ),
        "DeleteRow": grpc.unary_unary_rpc_method_handler(
            servicer.DeleteRow,
            request_deserializer=google_dot_cloud_dot_area120__tables__v1alpha1_dot_proto_dot_tables__pb2.DeleteRowRequest.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "google.area120.tables.v1alpha1.TablesService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class TablesService(object):
    """The Tables Service provides an API for reading and updating tables.
    It defines the following resource model:

    - The API has a collection of [Table][google.area120.tables.v1alpha1.Table]
    resources, named `tables/*`

    - Each Table has a collection of [Row][google.area120.tables.v1alpha1.Row]
    resources, named `tables/*/rows/*`
    """

    @staticmethod
    def GetTable(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/google.area120.tables.v1alpha1.TablesService/GetTable",
            google_dot_cloud_dot_area120__tables__v1alpha1_dot_proto_dot_tables__pb2.GetTableRequest.SerializeToString,
            google_dot_cloud_dot_area120__tables__v1alpha1_dot_proto_dot_tables__pb2.Table.FromString,
            options,
            channel_credentials,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def ListTables(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/google.area120.tables.v1alpha1.TablesService/ListTables",
            google_dot_cloud_dot_area120__tables__v1alpha1_dot_proto_dot_tables__pb2.ListTablesRequest.SerializeToString,
            google_dot_cloud_dot_area120__tables__v1alpha1_dot_proto_dot_tables__pb2.ListTablesResponse.FromString,
            options,
            channel_credentials,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def GetRow(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/google.area120.tables.v1alpha1.TablesService/GetRow",
            google_dot_cloud_dot_area120__tables__v1alpha1_dot_proto_dot_tables__pb2.GetRowRequest.SerializeToString,
            google_dot_cloud_dot_area120__tables__v1alpha1_dot_proto_dot_tables__pb2.Row.FromString,
            options,
            channel_credentials,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def ListRows(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/google.area120.tables.v1alpha1.TablesService/ListRows",
            google_dot_cloud_dot_area120__tables__v1alpha1_dot_proto_dot_tables__pb2.ListRowsRequest.SerializeToString,
            google_dot_cloud_dot_area120__tables__v1alpha1_dot_proto_dot_tables__pb2.ListRowsResponse.FromString,
            options,
            channel_credentials,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def CreateRow(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/google.area120.tables.v1alpha1.TablesService/CreateRow",
            google_dot_cloud_dot_area120__tables__v1alpha1_dot_proto_dot_tables__pb2.CreateRowRequest.SerializeToString,
            google_dot_cloud_dot_area120__tables__v1alpha1_dot_proto_dot_tables__pb2.Row.FromString,
            options,
            channel_credentials,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def BatchCreateRows(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/google.area120.tables.v1alpha1.TablesService/BatchCreateRows",
            google_dot_cloud_dot_area120__tables__v1alpha1_dot_proto_dot_tables__pb2.BatchCreateRowsRequest.SerializeToString,
            google_dot_cloud_dot_area120__tables__v1alpha1_dot_proto_dot_tables__pb2.BatchCreateRowsResponse.FromString,
            options,
            channel_credentials,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def UpdateRow(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/google.area120.tables.v1alpha1.TablesService/UpdateRow",
            google_dot_cloud_dot_area120__tables__v1alpha1_dot_proto_dot_tables__pb2.UpdateRowRequest.SerializeToString,
            google_dot_cloud_dot_area120__tables__v1alpha1_dot_proto_dot_tables__pb2.Row.FromString,
            options,
            channel_credentials,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def BatchUpdateRows(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/google.area120.tables.v1alpha1.TablesService/BatchUpdateRows",
            google_dot_cloud_dot_area120__tables__v1alpha1_dot_proto_dot_tables__pb2.BatchUpdateRowsRequest.SerializeToString,
            google_dot_cloud_dot_area120__tables__v1alpha1_dot_proto_dot_tables__pb2.BatchUpdateRowsResponse.FromString,
            options,
            channel_credentials,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def DeleteRow(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/google.area120.tables.v1alpha1.TablesService/DeleteRow",
            google_dot_cloud_dot_area120__tables__v1alpha1_dot_proto_dot_tables__pb2.DeleteRowRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options,
            channel_credentials,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
